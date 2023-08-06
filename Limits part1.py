from manim import *
from math import floor


def truncate_decimal(num):
    truncated_num = floor(num * 100) / 100
    return truncated_num

class Scene1(Scene):
    def construct(self):
        # self.add(NumberPlane())
        title = Text("Limits" , color=BLUE).scale(0.7)
        numline = NumberLine(
            x_range=[-5, 5, 1],
            length=11,
            include_numbers=True,
            tick_size=0.08,
            font_size=25,
            line_to_number_buff=0.15
        )
        x = Triangle(fill_color = WHITE, fill_opacity = 1, stroke_width = 0).rotate(PI).scale(0.1).shift(DOWN * 0.185 + RIGHT * 4.4)
        xtext = MathTex(r"x").scale(0.7).next_to(x , UP , buff=0.15)

        self.wait()
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Create(numline))
        self.play(FadeIn(*[x , xtext]))
        self.play(x.animate.shift(LEFT * 2.197) , xtext.animate.shift(LEFT * 2.197) , rate_func = ease_out_cubic , run_time = 3)
        self.wait(0.5)
        self.play(x.animate.shift(LEFT * 2.203) , xtext.animate.shift(LEFT * 2.203) , run_time = 0.5)
        self.wait(0.5)
        self.play(x.animate.shift(RIGHT * 2.197) , xtext.animate.shift(RIGHT * 2.197) , rate_func = ease_out_cubic , run_time = 3)
        self.play(FadeOut(*[title , x , xtext]))
        self.wait()

class Scene2(Scene):
    def construct(self):
        # self.add(NumberPlane())
        numline = NumberLine(
            x_range=[-5, 5, 1],
            length=11,
            include_numbers=True,
            tick_size=0.08,
            font_size=25,
            line_to_number_buff=0.15
        )

        plane = NumberPlane(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057},
                            background_line_style={"stroke_color":GRAY ,"stroke_opacity":0.5 , "stroke_width":0.899}
                            )

        
        ax = Axes(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057}).add_coordinates()
        eqn = MathTex(r"f(" , "x" , r") = \frac{2}{3}" , "x" , color=GREEN).scale(0.65).move_to([-2.2,2.8,0])
        eqn[1].set_color(YELLOW)
        eqn[3].set_color(YELLOW)
        eqn2 = MathTex(r"f(" , "3" , ") = 2" , color = GREEN).scale(0.6).next_to(eqn , DOWN , buff=1.6 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
        eqn2[1].set_color(YELLOW)
        limeqn = MathTex(r"\lim_{" , r"x" ,  r"\to" , r"3}" , r"f(" , r"x" , r")" , r"=" , r"2" , color=BLUE).scale(0.65).next_to(eqn , DOWN , buff=1.7 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
        limeqn[1].set_color(GREEN)
        limeqn[5].set_color(GREEN)
        curve = ax.plot(lambda x : (2/3) * x , x_range=[-7,7] , stroke_width = 2)
        canvas = Square(2.1 , fill_color = BLACK , fill_opacity = 1 , stroke_width = 0).move_to(ax.coords_to_point(-2,2))
        value1 = ValueTracker(4)
        value2 = ValueTracker(2)

        point1 = always_redraw(lambda: Dot(ax.coords_to_point(value1.get_value(), (2/3) * value1.get_value()), color=BLUE) )
        lines1 = always_redraw(lambda: ax.get_lines_to_point(ax.c2p(value1.get_value(), (2/3) * value1.get_value())))

        point2 = always_redraw(lambda: Dot(ax.coords_to_point(value2.get_value(), (2/3) * value2.get_value()), color=BLUE) )
        lines2 = always_redraw(lambda: ax.get_lines_to_point(ax.c2p(value2.get_value(), (2/3) * value2.get_value())))

        
        self.add(numline)

        self.play(Transform(numline , plane))
        self.wait()
        self.play(FadeIn(canvas) , Write(eqn))
        self.play(Create(curve))
        self.wait()

        self.play(FadeIn(*[point1 , point2 , lines1 , lines2]))
        self.wait()

        self.play(value1.animate.set_value(3.01) , value2.animate.set_value(2.99) , rate_func = ease_out_cubic , run_time = 4)
        self.wait()
        self.play(Write(eqn2))

        self.play(FadeOut(eqn2))
        self.play(Write(limeqn))
        self.wait()
        self.play(ApplyWave(limeqn[0] , amplitude=0.1))
        self.play(Indicate(limeqn[1] , scale_factor = 1.3))
        self.play(Indicate(limeqn[3] , scale_factor = 1.3))
        self.play(Indicate(VGroup(limeqn[4] , limeqn[5] , limeqn[6]) , scale_factor = 1.3))
        self.play(Indicate(limeqn[8] , scale_factor = 1.3))


        self.play(FadeOut(*[canvas , limeqn , eqn , curve , point1 , point2 , lines1 , lines2]))
        

        self.wait()

class Scene3(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057},
                            background_line_style={"stroke_color":GRAY ,"stroke_opacity":0.5 , "stroke_width":0.899}
                            )
        
        ax = Axes(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057}).add_coordinates()
        canvas = Rectangle(fill_color=BLACK ,fill_opacity=1 , stroke_width=0 , height=2.1 , width=3.15).move_to(ax.coords_to_point(-2.5,2))
        eqn = MathTex(r"f(x)" , r"=", r"\frac{x-1}{x-1}").scale(0.65).move_to(ax.coords_to_point(-2.5,2.5))
        eqn2 = MathTex(r"={" , r"1", r"-1" ,  r"\over" ,  r"1" , r"-1}" , color=GREEN).scale(0.65).move_to(ax.coords_to_point(-2.16,1.5)).align_to(eqn[1] , LEFT)
        eqn3 = MathTex(r"={" , r"0",  r"\over" ,  r"0}" , color=GREEN).scale(0.65).move_to(ax.coords_to_point(-2.4,1.5)).align_to(eqn2 , LEFT)
        eqn[0].set_color(BLUE)
        eqn[2].set_color(GREEN)

        eqn2[1].set_color(YELLOW)
        eqn2[4].set_color(YELLOW)

        curve = ax.plot(lambda x: (x-1)/(x-1) , x_range=[-7,7] , color=BLUE)
        text = Tex("(Indeterminate Form)").scale(0.6).next_to(eqn2 , DOWN , buff=0.4)

        point1 = Dot(ax.coords_to_point(2,1) , color=BLUE)
        text1 = MathTex(r"(2,1)").scale(0.5).next_to(point1 , UP , buff=0.1)

        point2 = Dot(ax.coords_to_point(-5,1) , color=BLUE)
        text2 = MathTex(r"(-5,1)").scale(0.5).next_to(point2 , UP , buff=0.1)

        point3 = Dot(ax.coords_to_point(1,1) , radius=0.07 , stroke_width=1.9, color=BLACK , stroke_color=BLUE)
        text3 = MathTex(r"(1,undefined)").scale(0.5).next_to(point3 , UP , buff=0.1)

        eqn4 = MathTex(r"f(1) = undefined" , color=GREEN).scale(0.65).move_to(ax.coords_to_point(-2.14,1.48))

        limtext = MathTex(r"\lim_{x \to 1}" , r"f(x)" , r"=\;?" , color=GREEN).scale(0.6).next_to(eqn , DOWN , buff=0.45)
        limtext[1].set_color(BLUE)

        limtext2 = MathTex(r"\lim_{x \to 1}" , r"f(x)" , r"=" ,r"1" , color=GREEN).scale(0.6).next_to(eqn , DOWN , buff=0.45)
        limtext2[1].set_color(BLUE)
        limtext2[3].set_color(BLUE)
        
        self.add(plane)
        self.wait()
        self.play(FadeIn(canvas) , Write(eqn))
        self.play(Create(curve) , rate_func=linear)
        self.play(Indicate(eqn[2]))
        self.play(FadeIn(eqn2 , target_position=VGroup(eqn[1] , eqn[2])))
        self.play(TransformMatchingShapes(eqn2 , eqn3))
        self.play(Write(text))

        self.play(FadeIn(point1) , FadeIn(text1))
        self.wait()
        self.play(Transform(point1 , point2) , Transform(text1 , text2))
        self.wait()
        self.play(Transform(point1 , point3) , Transform(text1 , text3))

        self.play(TransformMatchingShapes(eqn3 , eqn4))
        self.play(FadeOut(*[eqn4 , point1 , text1 , text]))

        self.play(Write(limtext))
        self.wait()
        self.play(TransformMatchingTex(limtext , limtext2) , run_time = 1.5)

        self.play(FadeOut(*[canvas , limtext2 , curve , eqn]))


        
        
        self.wait()


class Scene4(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057},
                            background_line_style={"stroke_color":GRAY ,"stroke_opacity":0.5 , "stroke_width":0.899}
                            )
        
        ax = Axes(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057}).add_coordinates()
        
        eqn = MathTex(r"f(x)" , r"=" , r"\frac{1}{x}").scale(0.75).move_to(ax.coords_to_point(-2.5,2.5))
        eqn2 = MathTex(r"\lim_{x \to 0}" , r"f(x)" , r"=\;?").scale(0.7).next_to(eqn , DOWN , buff=0.5)
        eqn3 = MathTex(r"\lim_{x \to 0}" , r"f(x)" , r"=" , r"\infty").scale(0.7).next_to(eqn , DOWN , buff=0.5).align_to(eqn2 , LEFT)
        
        eqn3[0].set_color(GREEN)
        eqn3[1].set_color(BLUE)
        eqn3[3].set_color(YELLOW)

        eqn2[0].set_color(GREEN)
        eqn2[1].set_color(BLUE)

        eqn[0].set_color(BLUE)
        eqn[2].set_color(GREEN)

        curve1 = ax.plot(lambda x : (1/x) , x_range=[-7 , -0.1] , color=BLUE)
        curve2 = ax.plot(lambda x : (1/x) , x_range=[0.1 , 7] , color=BLUE).reverse_points()

        cross = Cross(eqn3[3] , stroke_width=3 , scale_factor=2)
        pointx = ValueTracker(3)

        point = always_redraw(lambda: Dot(ax.coords_to_point(pointx.get_value() , 1/pointx.get_value()) , color=BLUE))
        label = always_redraw(lambda: MathTex(f"({truncate_decimal(pointx.get_value())} , {truncate_decimal(1/pointx.get_value())})").scale(0.4).move_to(ax.coords_to_point(pointx.get_value() , 1/pointx.get_value()) + [0.35, 0.3, 0] ))

        pointx2 = ValueTracker(-3)

        point2 = always_redraw(lambda: Dot(ax.coords_to_point(pointx2.get_value() , 1/pointx2.get_value()) , color=BLUE))
        label2 = always_redraw(lambda: MathTex(f"({truncate_decimal(pointx2.get_value())} , {truncate_decimal(1/pointx2.get_value())})").scale(0.4).move_to(ax.coords_to_point(pointx2.get_value() , 1/pointx2.get_value()) - [0.35, 0.3, 0] ))

        rhl = Tex("Right hand limit:" , color=BLUE).scale(0.7).move_to([2.7 , 3 , 0])
        rhleqn = MathTex(r"\lim_{x \to 0 ^ {+}} f(x) = \infty" , color=GREEN).scale(0.7).next_to(rhl , DOWN).align_to(rhl , LEFT)

        lhl = Tex("Left hand limit:" , color=BLUE).scale(0.7).move_to([-4.4 , -1.1 , 0])
        lhleqn = MathTex(r"\lim_{x \to 0 ^ {-}} f(x) = -\infty" , color=GREEN).scale(0.7).next_to(lhl , DOWN).align_to(lhl , LEFT)

        dne = Tex("Does not exist!" , color=YELLOW).scale(0.65).move_to(eqn3[3]).align_to(eqn3[3] , LEFT)

        self.add(plane)

        self.wait()


        self.play(Write(eqn))
        self.play(Create(curve1) , Create(curve2) , run_time = 1.5)
        self.play(Write(eqn2))
        self.play(FadeIn(point) , FadeIn(label))
        self.play(pointx.animate.set_value(0.2) , rate_func = ease_out_cubic , run_time=5)
        self.play(TransformMatchingTex(eqn2 , eqn3))

        self.play(Create(cross))

        self.play(FadeIn(point2) , FadeIn(label2))
        self.play(pointx2.animate.set_value(-0.2) , rate_func = ease_out_cubic , run_time=5)

        self.play(Write(rhl))
        self.play(Write(rhleqn) , run_time = 2)
        self.play(Write(lhl))
        self.play(Write(lhleqn) , run_time = 2)

        self.play(Transform(VGroup(cross , eqn3[3]) , dne) )

        self.play(FadeOut(*[cross , eqn3 , eqn , curve1 , curve2 , lhl , rhl , lhleqn , rhleqn]))

        self.wait()


class Scene5(Scene):
    def construct(self):

        def left_function(x):
            return x+1
        

        def right_function(x):
            return ((x**3)-x+1)



        plane = NumberPlane(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057},
                            background_line_style={"stroke_color":GRAY ,"stroke_opacity":0.5 , "stroke_width":0.899}
                            )
        
        ax = Axes(x_range=[-8 , 8 , 1],
                            y_range=[-8 , 8 , 1],
                            x_length=17,
                            y_length=17,
                            axis_config={"include_numbers":True, "tick_size":0.08, "font_size":20, "line_to_number_buff":0.057}).add_coordinates()
        

        curve1 = ax.plot(left_function , x_range=[-7,-1] , color=BLUE , stroke_width=3)
        curve2 = ax.plot(right_function , x_range=[-1,7] , color=BLUE , stroke_width=3)
        
        lhs = MathTex(r"f(x)",  r" = ").scale(0.75).move_to([-5.5 , 3 ,0])
        lhs[0].set_color(BLUE)

        rhs1 = MathTex(r"x+1" , r"\quad \quad \quad \;\; (for \; x \le -1)").scale(0.7).next_to(lhs , RIGHT, buff=0.6).shift(UP * 0.3)
        rhs2 = MathTex(r"x^{3}-x+1" , r"\quad \; (for \; x > -1)").scale(0.7).next_to(lhs , RIGHT, buff=0.6).shift(DOWN * 0.3)

        brace = Brace(VGroup(rhs1 , rhs2) , LEFT, sharpness=2, buff=0.1 , color=BLUE_B)

        rhs1[0].set_color(GREEN)
        rhs2[0].set_color(GREEN)

        rhs1[1].shift(LEFT * 0.01)

        tracker1 = ValueTracker(-0.3)
        point1 = always_redraw(lambda: Dot(ax.coords_to_point(tracker1.get_value() , right_function(tracker1.get_value())) , color=BLUE) )

        tracker2 = ValueTracker(-2)
        point2 = always_redraw(lambda: Dot(ax.coords_to_point(tracker2.get_value() , left_function(tracker2.get_value())) , color=BLUE) )

        limeqn1 = MathTex(r"\lim_{x \to -1^{+}}" ,  r"f(x)"  , r"=" , r"1").scale(0.7).move_to([3.3 , 2.2 , 0])
        limeqn1[0].set_color(GREEN)
        limeqn1[1].set_color(BLUE)
        limeqn1[3].set_color(GREEN)

        limeqn2 = MathTex(r"\lim_{x \to -1^{ \small -}}" ,  r"f(x)"  , r"=" , r"0").scale(0.7).move_to([-4.4 , -1.1 , 0])
        limeqn2[0].set_color(GREEN)
        limeqn2[1].set_color(BLUE)
        limeqn2[3].set_color(GREEN)

        limeqn3 = MathTex(r"\lim_{x \to -1}" ,  r"f(x)\; Does\;not\;exist!" , color=RED).scale(0.9).move_to([3.2 , -1.1 , 0])



        self.add(plane)
        self.wait()
        self.play(Write(lhs))
        self.play(FadeIn(brace) ,Write(rhs1) , Write(rhs2))
        self.play(Create(curve1) , rate_func = linear)
        self.play(Create(curve2) , rate_func = linear)
        self.play(FadeIn(point1))
        self.play(tracker1.animate.set_value(-1.001) , rate_func = ease_out_cubic , run_time = 3)
        self.wait()
        self.play(Write(limeqn1))
        self.wait()

        self.play(TransformMatchingShapes(point1 , point2))
        self.play(tracker2.animate.set_value(-1) , rate_func = ease_out_cubic , run_time = 3)
        self.wait()
        self.play(Write(limeqn2))
        self.wait()

        self.play(Write(limeqn3))


        


        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
