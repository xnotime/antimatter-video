from manim import *
from manim_chemistry import *

def readmol(name: str) -> GraphMolecule:
    return GraphMolecule.build_from_mol(
        mol_file= f'mol/{name}.h.mol',
        label= True,
    )



class Top(Scene):
    def construct(self):
        mol0 = Group(
            readmol('BoricAcid').scale(0.8).shift(UP + (5 * LEFT)),
            readmol('BoricAcid').scale(0.8).shift((1.333 * DOWN) + (1.333 * LEFT)),
            readmol('BoricAcid').scale(0.8).shift((1.333 * UP) + (1.333 * RIGHT)),
            readmol('BoricAcid').scale(0.8).shift(DOWN + (5 * RIGHT)),
        )
        mol1 = Group(
            readmol('MetaboricAcid').scale(0.8).shift(UP + (5 * LEFT)),
            readmol('MetaboricAcid').scale(0.8).shift((1.333 * DOWN) + (1.333 * LEFT)),
            readmol('MetaboricAcid').scale(0.8).shift((1.333 * UP) + (1.333 * RIGHT)),
            readmol('MetaboricAcid').scale(0.8).shift(DOWN + (5 * RIGHT)),
        )
        mol2 = Group(
            readmol('TetraboricAcid'),
        )
        mol3 = Group(
            readmol('BoricOxide').scale(0.8).shift((1.333 * DOWN) + (1.333 * LEFT)),
            readmol('BoricOxide').scale(0.8).shift((1.333 * UP) + (1.333 * RIGHT)),
        )
        self.add(mol0)
        self.wait(1)
        self.play(LaggedStart(
            (
                AnimationGroup(FadeOut(mol0[i]), FadeIn(mol1[i]))
                for i in range(4)
            ),
            lag_ratio= 0.1,
        ))
        self.wait(1)
        self.play(
            mol1[0].animate.shift(-(UP + (5 * LEFT))).set_opacity(0),
        )
