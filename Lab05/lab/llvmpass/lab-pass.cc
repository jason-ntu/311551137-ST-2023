/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/IRBuilder.h"

using namespace llvm;

char LabPass::ID = 0;

bool LabPass::doInitialization(Module &M) {
  return true;
}

static Constant* getI8StrVal(Module &M, char const *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();

  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
    GlobalValue::InternalLinkage, strConstant, name);

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = { zero, zero };
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
    gvStr, indices, true);

  return strVal;
}


static FunctionCallee printfPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  FunctionType *printfType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt8PtrTy(ctx) },
    true);

  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfType);

  return printfCallee;
}

bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";

  LLVMContext &ctx = M.getContext();
  FunctionCallee printfCallee = printfPrototype(M);

  // Constant* space = ConstantDataArray::getString(ctx, " ");
  Constant* space = ConstantInt::get(Type::getInt32Ty(ctx), ' ');
  Constant* zero = ConstantInt::getSigned(Type::getInt32Ty(ctx), 0);
  Constant* one = ConstantInt::getSigned(Type::getInt32Ty(ctx), 1);

  GlobalVariable * depth = new GlobalVariable(M, Type::getInt32Ty(ctx), false, GlobalValue::ExternalLinkage, zero);

  for (auto &F : M) {
    if (F.empty()) {
      continue;
    }
    
    // Set prologue 
    BasicBlock &Bstart = F.front();
    Instruction &Istart = Bstart.front();
    IRBuilder<> BuilderStart(&Istart);

    // Increase depth by 1
    LoadInst* oldDepth = BuilderStart.CreateLoad(Type::getInt32Ty(ctx), depth);
    Value* newDepth = BuilderStart.CreateAdd(oldDepth, one);
    BuilderStart.CreateStore(newDepth, depth);

    // Get function name and address
    std::string funcName = F.getName().str().c_str();

    // Print message
    if (funcName == (std::string) "main") {
      Constant *msg = getI8StrVal(M, (funcName + ": %p\n").c_str(), "msg");
      BuilderStart.CreateCall(printfCallee, { msg, &F });
    } else {
      Constant *msg = getI8StrVal(M, ("%*c" + funcName + ": %p\n").c_str(), "msg");
      BuilderStart.CreateCall(printfCallee, { msg, oldDepth, space, &F });
    }

    // Create epilogue BB before ret BB
    BasicBlock &Bend = F.back();
    Instruction &ret = *(++Bend.rend());
    BasicBlock *Bret = Bend.splitBasicBlock(&ret, "ret");
    BasicBlock *Bepi = BasicBlock::Create(ctx, "epi", &F, Bret);

    // Branch to epilogue BB
    Instruction &br = *(++Bend.rend());
    IRBuilder<> BuilderBr(&br);
    BuilderBr.CreateBr(Bepi);
    br.eraseFromParent();

    // Reset depth
    IRBuilder<> BuilderEnd(Bepi);
    BuilderEnd.CreateStore(oldDepth, depth);

    // Branch to ret BB
    BuilderEnd.CreateBr(Bret);

  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);