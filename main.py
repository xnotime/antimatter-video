from manim import *
from manim_chemistry import *

def readmol(name: str) -> GraphMolecule:
    return GraphMolecule.build_from_mol(
        mol_file= f'mol/{name}.h.mol',
        label= True,
    )

class Top(Scene):
    def construct(self):
        left0 = MathTex('< 140\\,{}^{\\circ} \\text{C}').to_corner(UP + LEFT)
        left1 = MathTex('< 180\\,{}^{\\circ} \\text{C}').to_corner(UP + LEFT)
        left2 = MathTex('< 530\\,{}^{\\circ} \\text{C}').to_corner(UP + LEFT)
        left3 = MathTex('> 530\\,{}^{\\circ} \\text{C}').to_corner(UP + LEFT)

        right0 = Tex('Boric Acid').to_corner(UP + RIGHT)
        right1 = Tex('Metaboric Acid').to_corner(UP + RIGHT)
        right2 = Tex('Pyroboric Acid').to_corner(UP + RIGHT)
        right3 = Tex('Boric Oxide').to_corner(UP + RIGHT)

        mol0 = Group(
            readmol('BoricAcid').scale(0.85).shift(UP + (5 * LEFT)),
            readmol('BoricAcid').scale(0.85).shift((1.333 * DOWN) + (1.333 * LEFT)),
            readmol('BoricAcid').scale(0.85).shift((1.333 * UP) + (1.333 * RIGHT)),
            readmol('BoricAcid').scale(0.85).shift(DOWN + (5 * RIGHT)),
        )
        mol1 = Group(
            readmol('MetaboricAcid').scale(1.2).shift(UP + (5 * LEFT)),
            readmol('MetaboricAcid').scale(1.2).shift((1.333 * DOWN) + (1.333 * LEFT)),
            readmol('MetaboricAcid').scale(1.2).shift((1.333 * UP) + (1.333 * RIGHT)),
            readmol('MetaboricAcid').scale(1.2).shift(DOWN + (5 * RIGHT)),
        )
        mol2 = Group(
            readmol('TetraboricAcid').scale(1.2),
        )
        mol3 = Group(
            readmol('BoricOxide').scale(1.2).shift((1.333 * DOWN) + (1.333 * LEFT)),
            readmol('BoricOxide').scale(1.2).shift((1.333 * UP) + (1.333 * RIGHT)),
        )
        self.play(FadeIn(mol0), Write(left0), Write(right0))
        self.wait(1)
        self.play(Transform(left0, left1), Transform(right0, right1), LaggedStart(
            (
                AnimationGroup(FadeOut(mol0[i]), FadeIn(mol1[i]))
                for i in range(4)
            ),
            lag_ratio= 0.15,
        ))
        self.wait(1)
        self.play(Transform(left0, left2), Transform(right0, right2), LaggedStart(
            [
                LaggedStart(
                    [
                        mol1[0].animate.shift(-(UP + (5 * LEFT))).set_opacity(0),
                        mol1[1].animate.shift(-((1.333 * DOWN) + (1.333 * LEFT))).set_opacity(0),
                        mol1[2].animate.shift(-((1.333 * UP) + (1.333 * RIGHT))).set_opacity(0),
                        mol1[3].animate.shift(-(DOWN + (5 * RIGHT))).set_opacity(0),
                    ],
                    lag_ratio= 0.05
                ),
                FadeIn(mol2[0]),
            ],
            lag_ratio= 0.1,
        ))
        self.wait(1)
        self.play(Transform(left0, left3), Transform(right0, right3), LaggedStart(
            [
                FadeOut(mol2[0]),
                FadeIn(mol3[0]),
                FadeIn(mol3[1]),
            ],
            lag_ratio= 0.15
        ))
        self.wait(1)
        self.play(LaggedStart(
            [
                LaggedStart(
                    [
                        mol3[0].get_atoms_vgroup_from_index([3]).animate.set_opacity(0),
                        mol3[0].get_bonds_vgroup_from_index([1], 0)[1].animate.set_opacity(0),
                        mol3[0].get_bonds_vgroup_from_index([1], 0)[0].animate.set_opacity(0),
                        mol3[0].get_atoms_vgroup_from_index([2]).animate.set_opacity(0),
                        mol3[0].get_bonds_vgroup_from_index([4], 0)[0].animate.set_opacity(0),
                        mol3[0].get_bonds_vgroup_from_index([4], 0)[1].animate.set_opacity(0),
                        mol3[0].get_atoms_vgroup_from_index([5]).animate.set_opacity(0),
                    ],
                    lag_ratio= 0.1,
                ),
                LaggedStart(
                    [
                        mol3[1].get_atoms_vgroup_from_index([3]).animate.set_opacity(0),
                        mol3[1].get_bonds_vgroup_from_index([1], 0)[1].animate.set_opacity(0),
                        mol3[1].get_bonds_vgroup_from_index([1], 0)[0].animate.set_opacity(0),
                        mol3[1].get_atoms_vgroup_from_index([2]).animate.set_opacity(0),
                        mol3[1].get_bonds_vgroup_from_index([4], 0)[0].animate.set_opacity(0),
                        mol3[1].get_bonds_vgroup_from_index([4], 0)[1].animate.set_opacity(0),
                        mol3[1].get_atoms_vgroup_from_index([5]).animate.set_opacity(0),
                    ],
                    lag_ratio= 0.1,
                ),
            ],
            lag_ratio= 0.08,
        ))
        self.wait(1)
        proton = lambda: \
            Dot(radius= 0.7, color= ManimColor('#FF0000'))
        neutron = lambda: \
            Dot(radius= 0.7, color= ManimColor('#0000FF'))
        sc = 3.5
        nuc_10b = VGroup(
            proton().shift(sc*((+0.1 * UP) + (-0.2 * LEFT))),
            neutron().shift(sc*((-0.1 * UP) + (-0.1 * LEFT))),
            neutron().shift(sc*((+0.3 * UP) + (-0.1 * LEFT))),
            proton().shift(sc*((-0.2 * UP) + (+0.1 * LEFT))),
            proton().shift(sc*((-0.1 * UP) + (-0.1 * LEFT))),
            neutron().shift(sc*((-0.1 * UP) + (+0.2 * LEFT))),
            neutron().shift(sc*((+0.3 * UP) + (+0.1 * LEFT))),
            proton().shift(sc*((+0.2 * UP) + (+0.1 * LEFT))),
            proton().shift(sc*((+0.1 * UP) + (-0.3 * LEFT))),
            neutron().shift(sc*((-0.1 * UP) + (+0.2 * LEFT))),
        ).shift(3 * LEFT)
        nuc_11b = VGroup(
            proton().shift(sc*((+0.1 * UP) + (-0.3 * LEFT))),
            neutron().shift(sc*((-0.1 * UP) + (+0.2 * LEFT))),
            neutron().shift(sc*((-0.1 * UP) + (+0.2 * LEFT))),
            proton().shift(sc*((+0.2 * UP) + (+0.1 * LEFT))),
            neutron().shift(sc*((+0.3 * UP) + (+0.1 * LEFT))),
            neutron().shift(sc*((-0.1 * UP) + (-0.1 * LEFT))),
            neutron().shift(sc*((+0.3 * UP) + (-0.1 * LEFT))),
            proton().shift(sc*((-0.2 * UP) + (+0.1 * LEFT))),
            proton().shift(sc*((+0.1 * UP) + (-0.2 * LEFT))),
            neutron().shift(sc*((-0.2 * UP) + (-0.1 * LEFT))),
            proton().shift(sc*((-0.1 * UP) + (-0.1 * LEFT))),
        ).shift(3 * RIGHT)
        self.play(VGroup(*mol3, left0, right0).animate.scale(5.0, about_point= ORIGIN).set_opacity(0), run_time=0.75)
        self.play(Create(nuc_10b), Create(nuc_11b), run_time=0.25)
        self.wait(1)
