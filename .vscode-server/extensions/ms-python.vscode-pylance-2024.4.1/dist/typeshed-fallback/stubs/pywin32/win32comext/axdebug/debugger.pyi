from _typeshed import Incomplete

from win32com.axdebug import contexts as contexts, documents, gateways as gateways
from win32com.axdebug.util import trace as trace
from win32com.axscript import axscript as axscript

currentDebugger: Incomplete

class ModuleTreeNode:
    moduleName: Incomplete
    module: Incomplete
    realNode: Incomplete
    cont: Incomplete
    def __init__(self, module) -> None: ...
    def Attach(self, parentRealNode) -> None: ...
    def Close(self) -> None: ...

def BuildModule(module, built_nodes, rootNode, create_node_fn, create_node_args) -> None: ...
def RefreshAllModules(builtItems, rootNode, create_node, create_node_args) -> None: ...

class CodeContainerProvider(documents.CodeContainerProvider):
    axdebugger: Incomplete
    currentNumModules: Incomplete
    nodes: Incomplete
    def __init__(self, axdebugger) -> None: ...
    def FromFileName(self, fname): ...
    def Close(self) -> None: ...

class OriginalInterfaceMaker:
    cookie: Incomplete
    def MakeInterfaces(self, pdm): ...
    def CloseInterfaces(self, pdm) -> None: ...

class SimpleHostStyleInterfaceMaker:
    def MakeInterfaces(self, pdm): ...
    def CloseInterfaces(self, pdm) -> None: ...

class AXDebugger:
    pydebugger: Incomplete
    pdm: Incomplete
    interfaceMaker: Incomplete
    expressionCookie: Incomplete
    def __init__(self, interfaceMaker: Incomplete | None = ..., processName: Incomplete | None = ...) -> None: ...
    def Break(self) -> None: ...
    app: Incomplete
    root: Incomplete
    def Close(self) -> None: ...
    def RefreshAllModules(self, nodes, containerProvider) -> None: ...
    def CreateApplicationNode(self, node, containerProvider): ...

def Break() -> None: ...

brk = Break
set_trace = Break

def dosomethingelse() -> None: ...
def dosomething() -> None: ...
def test() -> None: ...
