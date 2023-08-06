from manim import *

def video_icon():
    t = Triangle(stroke_color=WHITE , fill_color=WHITE, fill_opacity = 1).rotate(-PI/2).scale(0.5).shift(RIGHT * 0.1 + DOWN * 0.25)
    box = RoundedRectangle(stroke_color=DARK_BLUE , fill_color=DARK_BLUE, fill_opacity = 1, corner_radius=0.4 , width=2, height=1.7)
    return VGroup(box,t)

class Scene1(Scene):
    def construct(self):
        title = Text("Welcome back!" , color=BLUE).scale(0.7)
        limits = Text("Limits: " , color=GREEN).scale(0.45)
        icon1 = video_icon().scale(0.4)
        icon2 = video_icon().scale(0.4)
        tert = Text("Evaluate limits without graphing!").scale(0.52)

        sec = VGroup(limits , icon1 , icon2).arrange(RIGHT).shift(UP * 2)

        self.play(Write(title))
        self.play(title.animate.to_edge(UP) , FadeIn(sec))
        self.play(Circumscribe(sec[2] , stroke_width=2) , run_time = 2)
        self.play(Write(tert))

        self.play(FadeOut(*[title , sec , tert]))

        self.wait()

class Scene2(Scene):
    def construct(self):
        fn = MathTex(r"f(x)" , r"=" , r"{x" , r"-1" , r"\over" , r"x" , r"-1}").scale(0.9).to_edge(UP)
        fn[0].set_color(BLUE)
        fn[2].set_color(YELLOW)
        fn[3].set_color(GREEN)
        fn[4].set_color(GREEN)
        fn[5].set_color(YELLOW)
        fn[6].set_color(GREEN)

        qn = MathTex(r"\lim_{x \to 1}" , r"f(x)" , r"=\; ?").scale(0.7).shift(UP * 1.3)
        qn[0].set_color(GREEN)
        qn[1].set_color(BLUE)


        qn2 = MathTex(r"\lim_{x \to 1}" , r"f(x)" , r"=" , r"\lim_{x \to 1}" , r"{x" , r"-1" , r"\over" , r"x" , r"-1}").scale(0.7).move_to(qn)
        qn2[0].set_color(GREEN)
        qn2[1].set_color(BLUE)
        qn2[3].set_color(GREEN)
        qn2[4].set_color(YELLOW)
        qn2[5].set_color(GREEN)
        qn2[6].set_color(GREEN)
        qn2[7].set_color(YELLOW)
        qn2[8].set_color(GREEN)

        c1 = Cross(VGroup(qn2[4] , qn2[5]) , stroke_width=2)
        c2 = Cross(VGroup(qn2[7] , qn2[8]) , stroke_width=2)

        ans1 = MathTex(r"=" , r"{1" , r"-1" , r"\over" , r"1" , r"-1}").scale(0.7).next_to(qn2 , DOWN, buff=0.4).align_to(qn2[2] , LEFT)
        ans1[1].set_color(YELLOW)
        ans1[2].set_color(GREEN)
        ans1[3].set_color(GREEN)
        ans1[4].set_color(YELLOW)
        ans1[5].set_color(GREEN)


        ans2 = MathTex(r"=" , r"{0 \over 0}" , color = GREEN).scale(0.7).next_to(ans1 , DOWN, buff=0.4).align_to(qn2[2] , LEFT)
        ans2[0].set_color(WHITE)

        ans3 = MathTex(r"=" , r"1" , color = GREEN).scale(0.7).next_to(qn2 , DOWN, buff=0.4).align_to(qn2[2] , LEFT)
        ans3[0].set_color(WHITE)


        hint1 = Tex("(Substitution)" , color=BLUE).scale(0.6).next_to(ans1 , RIGHT , buff=0.3)

        indeter = Tex("Indeterminate forms:" , color=RED).scale(0.6).move_to([-5 , 3,0])


        i1 = MathTex(r"\to \frac{0}{0}").scale(0.5).next_to(indeter , DOWN , buff = 0.35).align_to(indeter , LEFT)
        i2 = MathTex(r"\to \frac{\infty}{\infty}").scale(0.5).next_to(i1 , DOWN , buff=0.35).align_to(indeter , LEFT)
        i3 = MathTex(r"\to \infty - \infty").scale(0.5).next_to(i2 , DOWN , buff=0.35).align_to(indeter , LEFT)
        i4 = MathTex(r"\to 0 \times \infty").scale(0.5).next_to(i3 , DOWN , buff=0.35).align_to(indeter , LEFT)
        i5 = MathTex(r"\to 0^{0}").scale(0.5).next_to(i4 , DOWN , buff=0.35).align_to(indeter , LEFT)
        i6 = MathTex(r"\to \infty^{0}").scale(0.5).next_to(i5 , DOWN , buff=0.35).align_to(indeter , LEFT)
        i7 = MathTex(r"\to 1^{\infty}").scale(0.5).next_to(i6 , DOWN , buff=0.35).align_to(indeter , LEFT)

        self.play(Write(fn))
        self.wait()
        self.play(Write(qn))
        self.play(TransformMatchingTex(qn , qn2))
        self.play(Write(ans1))
        self.play(Write(hint1))

        self.play(Write(indeter))
        self.play(Write(i1))
        self.play(Write(i2))
        self.play(Write(i3))
        self.play(Write(i4))
        self.play(Write(i5))
        self.play(Write(i6))
        self.play(Write(i7))


        self.play(Write(ans2))

        self.play(FadeOut(*[ans2 , ans1 , hint1]))
        self.play(AnimationGroup(*[Create(c1[0]) , Create(c2[0])] , lag_ratio=0.4)  )

        self.play(Write(ans3))

        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class Scene3(Scene):
    def construct(self):
        qn = MathTex(r"\lim_{x \to \; -5}" , r"{x" , r"^{2} - 25 \over" , r"x" , r"^{2} + 2" , r"x" , r"- 15}").scale(0.7).shift(UP * 2)
        qn[0].set_color(GREEN)
        qn[1].set_color(YELLOW)
        qn[2].set_color(GREEN)
        qn[3].set_color(YELLOW)
        qn[4].set_color(GREEN)
        qn[5].set_color(YELLOW)
        qn[6].set_color(GREEN)


        ans1 = MathTex(r"=" , r"{(-5)" , r"^{2} - 25 \over" , r"(-5)" , r"^{2} + 2" , r"(-5)" , r"- 15}").scale(0.7).next_to(qn , DOWN , buff=0.45).align_to(qn , LEFT)
        # ans1[1].set_color(GREEN)
        ans1[1].set_color(YELLOW)
        ans1[2].set_color(GREEN)
        ans1[3].set_color(YELLOW)
        ans1[4].set_color(GREEN)
        ans1[5].set_color(YELLOW)
        ans1[6].set_color(GREEN)

        ans2 = MathTex(r"=" , r"{0 \over 0}").scale(0.7).next_to(ans1 , DOWN , buff=0.35).align_to(qn , LEFT)
        # ans1[1].set_color(GREEN)
        ans2[1].set_color(GREEN)



        sans1 = MathTex(r"=" , r"\lim_{x \to \; -5}" , r"{(" , r"x" , r" - 5) \cdot" , r"(" , r"x" , r"+5)" ,  r"\over" , r"(" , r"x" , r" - 3) \cdot" , r"(" , r"x" , r"+5)}").scale(0.7).next_to(qn , DOWN , buff=0.45).align_to(qn , LEFT).shift(LEFT * 0.5)
        # ans1[1].set_color(GREEN)
        sans1[1].set_color(GREEN)
        sans1[2].set_color(GREEN)
        sans1[3].set_color(YELLOW)
        sans1[4].set_color(GREEN)
        sans1[5].set_color(GREEN)
        sans1[6].set_color(YELLOW)
        sans1[7].set_color(GREEN)
        sans1[8].set_color(GREEN)
        sans1[9].set_color(GREEN)
        sans1[10].set_color(YELLOW)
        sans1[11].set_color(GREEN)
        sans1[12].set_color(GREEN)
        sans1[13].set_color(YELLOW)
        sans1[14].set_color(GREEN)



        sans2 = MathTex(r"=" , r"{(-5)" , r"-5" ,   r"\over", r"(-5)" , r"-3}").scale(0.7).next_to(sans1 , DOWN , buff=0.45).align_to(sans1 , LEFT)
        # ans1[1].set_color(GREEN)
        sans2[1].set_color(YELLOW)
        sans2[2].set_color(GREEN)
        sans2[3].set_color(GREEN)
        sans2[4].set_color(YELLOW)
        sans2[5].set_color(GREEN)

        sans3 = MathTex(r"=" , r"{5 \over 4}").scale(0.7).next_to(sans2 , DOWN , buff=0.45).align_to(sans1 , LEFT)
        sans3[1].set_color(GREEN)

        cross1 = Cross(VGroup(sans1[5] , sans1[6] , sans1[7]) , stroke_width=2)
        cross2 = Cross(VGroup(sans1[12] , sans1[13] , sans1[14]) , stroke_width=2)

        

        self.play(Write(qn))
        self.play(Write(ans1))
        self.play(Write(ans2))
        self.play(FadeOut(*[ans1 , ans2]))
        self.play(Write(sans1))
        self.play(AnimationGroup(*[Create(cross1[0]) , Create(cross2[0]) ] , lag_ratio=0.4) )
        self.play(Write(sans2))
        self.play(Write(sans3))

        


        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )



class Scene4(Scene):
    def construct(self):
        # self.add(NumberPlane())
        qn = MathTex(r"\lim_{x \to 0}" , r"{x" , r"\over 3 - " , r"\sqrt{" ,  r"{x}" , r" + 9}}").scale(0.7).shift(UP * 2)
        qn[0].set_color(GREEN)
        qn[1].set_color(YELLOW)
        qn[2].set_color(GREEN)
        qn[3].set_color(GREEN)
        qn[4].set_color(YELLOW)
        qn[5].set_color(GREEN)

        ans1 = MathTex(r"=" , r"{0" , r"\over 3 - " , r"\sqrt{" ,  r"{0}" , r" + 9}}").scale(0.7).next_to(qn , DOWN , buff=0.45).align_to(qn , LEFT)
        ans1[1].set_color(YELLOW)
        ans1[2].set_color(GREEN)
        ans1[3].set_color(GREEN)
        ans1[4].set_color(YELLOW)
        ans1[5].set_color(GREEN)

        ans2 = MathTex(r"=" , r"{0 \over 0}").scale(0.7).next_to(ans1 , DOWN , buff=0.45).align_to(qn , LEFT)
        ans2[1].set_color(GREEN)

        rans1 = MathTex(r"=", r"\lim_{x \to 0}" , r"{x" , r"\over 3 - " , r"\sqrt{" ,  r"{x}" , r" + 9}}" , r"\times" , r"{3 + \sqrt{x + 9}" , r"\over 3 + " , r"\sqrt{" ,  r"{x}" , r" + 9}}").scale(0.7).next_to(qn , DOWN , buff=0.45).align_to(qn , LEFT).shift(LEFT * 0.35)
        rans1[1].set_color(GREEN)
        rans1[2].set_color(YELLOW)
        rans1[3].set_color(GREEN)
        rans1[4].set_color(GREEN)
        rans1[5].set_color(YELLOW)
        rans1[6].set_color(GREEN)


        # rans2 = MathTex(r"=", r"\lim_{x \to 0}" , r"{x" , r"\cdot (3 + \sqrt{" , r"{x}" , r"+ 9})" , r"\over 3^{2} -" , r"(\sqrt{" ,  r"{x}" , r" + 9})" , r")^{2} }").scale(0.7).next_to(rans1 , DOWN , buff=0.45).align_to(rans1 , LEFT)

        rans2 = MathTex(r"=", r"\lim_{x \to 0}" ,  r"{x" , r"\cdot (3 +" ,  r"\sqrt{" , r"{x}" , r"+ 9})" , r"\over 3^{2} - (" ,  r"\sqrt{" , r"{x}" , r"+ 9}) ^{2} }", color=GREEN).scale(0.7).next_to(rans1 , DOWN , buff=0.45).align_to(rans1 , LEFT)
        rans2[0].set_color(WHITE)
        rans2[2].set_color(YELLOW)
        rans2[5].set_color(YELLOW)
        rans2[9].set_color(YELLOW)

        hint = Tex("(Rationalization)" , color = BLUE).scale(0.6).next_to(rans1 , RIGHT)

        rans3 = MathTex(r"=", r"\lim_{x \to 0}" ,  r"{x" , r"\cdot (3 +" ,  r"\sqrt{" , r"{x}" , r"+ 9})" , r"\over" , r"9" , r"-" ,  r"{x}" , r"-" , r"9}", color=GREEN).scale(0.7).next_to(rans1 , DOWN , buff = 0.45).align_to(rans1 , LEFT)
        rans3[0].set_color(WHITE)
        rans3[2].set_color(YELLOW)
        rans3[5].set_color(YELLOW)
        rans3[10].set_color(YELLOW)
        c1 = Cross(rans3[8] , stroke_width=2).scale([2.5,1,1])
        c2 = Cross(rans3[12] , stroke_width=2).scale([2.5,1,1])
        c3 = Cross(rans3[2] , stroke_width=2).scale([2.5,1,1])
        c4 = Cross(rans3[10] , stroke_width=2).scale([2.5,1,1])



        rans4 = MathTex(r"=", r"\lim_{x \to 0}" , r"\;-(3 +" ,  r"\sqrt{" , r"{x}" , r"+ 9})" , color=GREEN).scale(0.7).next_to(rans1 , DOWN , buff = 0.45).align_to(rans1 , LEFT)
        rans4[0].set_color(WHITE)
        rans4[4].set_color(YELLOW)


        rans5 = MathTex(r"=", r"\;-(3 +" ,  r"\sqrt{" , r"{0}" , r"+ 9})" , color=GREEN).scale(0.7).next_to(rans4 , DOWN , buff = 0.45).align_to(rans1 , LEFT)
        rans5[0].set_color(WHITE)
        rans5[3].set_color(YELLOW)

        rans6 = MathTex(r"=", r"-6" , color=GREEN).scale(0.7).next_to(rans5 , DOWN , buff = 0.45).align_to(rans1 , LEFT).shift(UP * 0.75)
        rans6[0].set_color(WHITE)

        self.play(Write(qn))
        self.play(Write(ans1))
        self.play(Write(ans2))
        self.play(FadeOut(*[ans1 , ans2]))
        self.play(Write(rans1))
        self.play(Write(hint))
        self.play(Write(rans2))
        self.play(TransformMatchingTex(rans2 , rans3))
        self.play(Create(c1[0]) , Create(c2[0]))
        self.play(FadeOut(*[c1[0] , c2[0] , rans3[8] , rans3[12] , rans3[11]]))
        self.play(Create(c3[0]) , Create(c4[0]))
        self.play(TransformMatchingShapes(VGroup(rans3[0],
                                              rans3[1],
                                              rans3[2],
                                              rans3[3],
                                              rans3[4],
                                              rans3[5],
                                              rans3[6],
                                              rans3[7],
                                              rans3[9],
                                              rans3[10],
                                              )  , rans4) , FadeOut(*[c3[0] , c4[0]]))
        
        self.play(Write(rans5))
        animations = [
            qn.animate.shift(UP * 0.75),
            rans1.animate.shift(UP * 0.75),
            hint.animate.shift(UP * 0.75),
            rans4.animate.shift(UP * 0.75),
            rans5.animate.shift(UP * 0.75),
            Write(rans6)
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.2))

        



        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class Scene5(Scene):
    def construct(self):
        title = Text("What are the methods?" , color=BLUE).scale(0.7).to_edge(UP)
        subs = Text("Substitution").scale(0.55)
        fac =  Text("Factorization").scale(0.55)
        rat =  Text("Rationalization").scale(0.55)
        trig =  Text("Trigonometric identities").scale(0.55)
        sp =  Text("Special formulas").scale(0.55)
        dot1 =  MathTex(r"\cdot").scale(0.75)
        dot2 =  MathTex(r"\cdot").scale(0.75)

        methods = VGroup(subs , fac , rat , trig , sp , dot1 , dot2).arrange(DOWN)

        

        self.wait
        self.play(Write(title))
        self.play(Write(methods[0]))
        self.play(Write(methods[1]))
        self.play(Write(methods[2]))
        self.play(Write(methods[3]))
        self.play(Write(methods[4]))
        self.play(Write(methods[5]) , run_time = 0.3)
        self.play(Write(methods[6]) , run_time = 0.3)

        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class Scene6(Scene):
    def construct(self):
        title = Text("Piecewise Functions!" , color=BLUE).scale(0.75)

        lhs = MathTex(r"f(x)",  r" = ").scale(0.75)
        lhs[0].set_color(BLUE)

        rhs1 = MathTex(r"x" , r"+2" , r"\quad \quad \quad \;\; (for \; x \le -1)" , color=GREEN).scale(0.7).next_to(lhs , RIGHT, buff=0.6).shift(UP * 0.3)
        rhs2 = MathTex(r"x" , r"^{3}-" , r"x" , r"+1" , r"\quad \; (for \; x > -1)" , color=GREEN).scale(0.7).next_to(lhs , RIGHT, buff=0.6).shift(DOWN * 0.3)


        rhs1[0].set_color(YELLOW)
        rhs1[2].set_color(WHITE)


        rhs2[0].set_color(YELLOW)
        rhs2[2].set_color(YELLOW)
        rhs2[4].set_color(WHITE)

        rhs1[1].shift(LEFT * 0.01)

        rhs = VGroup(rhs1 , rhs2)
        brace = Brace(rhs , LEFT, sharpness=2, buff=0.1 , color=BLUE_B)

        func = VGroup(lhs , rhs , brace)
        func.move_to(ORIGIN).to_edge(UP)

        qn = MathTex(r"\lim_{x \to \; -1}" , r"f(x)" , r"=\;" , r"?" , color=GREEN).scale(0.7).shift(UP * 1.4)
        qn[1].set_color(BLUE)
        qn[2].set_color(WHITE)

        right_hand_limit_title = Tex("Right hand limit:", color=BLUE).scale(0.65).shift(UP*0.5 + RIGHT * 3)
        right_hand_limit_qn = MathTex(r"\lim_{x \to \; -1^{+}}" , r"x" , r"^{3}-" , r"x" , r"+1" , color=GREEN).scale(0.65).next_to(right_hand_limit_title , DOWN).align_to(right_hand_limit_title , LEFT)
        right_hand_limit_qn[1].set_color(YELLOW)
        right_hand_limit_qn[3].set_color(YELLOW)



        right_hand_limit_ans1 = MathTex(r"=" , r"(-1)" , r"^{3}-" , r"(-1)" , r"+1" , color=GREEN).scale(0.65).next_to(right_hand_limit_qn , DOWN).align_to(right_hand_limit_title , LEFT)
        right_hand_limit_ans1[0].set_color(WHITE)
        right_hand_limit_ans1[1].set_color(YELLOW)
        right_hand_limit_ans1[3].set_color(YELLOW)


        right_hand_limit_ans2 = MathTex(r"=" , r"1" , color=GREEN).scale(0.65).next_to(right_hand_limit_ans1 , DOWN).align_to(right_hand_limit_title , LEFT)
        right_hand_limit_ans2[0].set_color(WHITE)





        left_hand_limit_title = Tex("Left hand limit:", color=BLUE).scale(0.65).shift(UP * 0.5 + LEFT * 3)
        left_hand_limit_qn = MathTex(r"\lim_{x \to \; -1^{-}}" , r"x" , r"+2" , color=GREEN).scale(0.65).next_to(left_hand_limit_title , DOWN).align_to(left_hand_limit_title , LEFT)
        left_hand_limit_qn[1].set_color(YELLOW)



        left_hand_limit_ans1 = MathTex(r"=" , r"(-1)" ,  r"+2" , color=GREEN).scale(0.65).next_to(left_hand_limit_qn , DOWN).align_to(left_hand_limit_title , LEFT)
        left_hand_limit_ans1[0].set_color(WHITE)
        left_hand_limit_ans1[1].set_color(YELLOW)


        left_hand_limit_ans2 = MathTex(r"=" , r"1" , color=GREEN).scale(0.65).next_to(left_hand_limit_ans1 , DOWN).align_to(left_hand_limit_title , LEFT)
        left_hand_limit_ans2[0].set_color(WHITE)

        ans = MathTex(r"1" , color=GREEN).scale(0.7).move_to(qn[3])
        wrongans = MathTex(r"2" , color=RED).scale(0.65).move_to(left_hand_limit_ans2[1])
        dne = Tex("Does not exist!" , color=RED).scale(0.7).move_to(qn[3]).align_to(qn[3] , LEFT)

        self.wait()
        self.play(Write(title))
        self.play(Write(lhs) , FadeOut(title))
        self.play(Write(rhs1) , FadeIn(brace))
        self.play(Write(rhs2))
        self.play(Indicate(VGroup(rhs1[0] , rhs1[1])) )
        self.play(Indicate(VGroup(rhs2[0] , rhs2[1] , rhs2[2] , rhs2[3])) )
        self.play(Write(qn))
        self.wait()
        self.play(Write(right_hand_limit_title))
        self.wait()
        self.play(Indicate(VGroup(rhs2[0] , rhs2[1] , rhs2[2] , rhs2[3])) )
        self.play(Write(right_hand_limit_qn))
        self.play(Write(right_hand_limit_ans1))
        self.play(Write(right_hand_limit_ans2))


        self.play(Write(left_hand_limit_title))
        self.wait()
        self.play(Write(left_hand_limit_qn))
        self.play(Write(left_hand_limit_ans1))
        self.play(Write(left_hand_limit_ans2))
        self.play(FadeOut(qn[3]) , TransformFromCopy(VGroup(right_hand_limit_ans2[1] , left_hand_limit_ans2[1]) , ans))
        self.play(Transform(left_hand_limit_ans2[1] , wrongans))
        self.play(Transform(ans , dne))


        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
