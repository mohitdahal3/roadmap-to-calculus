from manim import *
from math import tan


class Scene1(Scene):
    def construct(self):
        welcome = Tex("Welcome back!", color=BLUE).scale(1.2)
        video_frame = Rectangle(color=YELLOW , height=4 , width=7)

        self.wait()
        self.play(Write(welcome))

        animations = [
            welcome.animate.to_edge(UP),
            Create(video_frame)
        ]
        self.play(AnimationGroup(*animations , lag_ratio=0.4))
        self.wait()
        self.play(FadeOut(welcome) , FadeOut(video_frame))

        self.wait()


class Scene2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        )
        line = ax.plot(lambda x:2*x , x_range=[-3.5,3.5] , color=BLUE)
        slope_text = Text("Slope = " , color=GREEN).move_to([-5,3,0]).scale(0.63)

        value = MathTex(r"[-\infty , \infty]" , color=GOLD).scale(0.8).next_to(slope_text , direction=RIGHT , buff=0.15)
        slope_text_new = Text("m = " , color=GREEN).scale(0.63).next_to(value , LEFT , buff=0.15)

        self.wait()

        self.play(Create(ax))
        self.play(Create(line))
        self.play(Rotate(line,-PI/4.5))
        self.wait()
        self.play(Rotate(line , PI/4.5))

        self.play(Write(slope_text))
        self.play(Write(value))
        self.play(Transform(slope_text,slope_text_new))


        


        self.wait()

class Scene3(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        )
        line = ax.plot(lambda x:2*x , x_range=[-3.5,3.5] , color=BLUE)
        slope_text = Text("Slope = " , color=GREEN).move_to([-5,3,0]).scale(0.63)
        value = MathTex(r"[-\infty , \infty]" , color=GOLD).scale(0.8).next_to(slope_text , direction=RIGHT , buff=0.15)
        slope_text_new = Text("m = " , color=GREEN).scale(0.63).next_to(value , LEFT , buff=0.15)

        angle = ValueTracker(0)
        line2 = always_redraw(lambda: Line(start=[-3,0,0] , end=[3,0,0] , buff=0 , color=BLUE).rotate(angle.get_value()) )
        
        # slope_value_number = always_redraw(lambda: MathTex(f"{round(tan(angle.get_value()) , 3) if(round(tan(angle.get_value()) , 3) < 10e+10) else 'infty'}" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15) )
        slope_value_number = always_redraw(lambda: MathTex(f"{round(tan(angle.get_value()) , 3)}" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15) if(abs( round(tan(angle.get_value()) , 3)) < 10e+10) else ( MathTex(r"\infty" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)))



        self.add(ax)
        self.add(line)
        self.add(slope_text_new)
        self.add(value)

        self.wait()
        self.play(ReplacementTransform(line , line2) , ReplacementTransform(value , slope_value_number))
        self.wait()

        self.play(angle.animate.set_value(PI/2) , rate_func=rush_from , run_time = 8)
        self.wait()
        self.play(angle.animate.set_value(PI) , run_time = 4)
        self.play(angle.animate.set_value(0) , run_time=0)
        self.wait()


        line = ax.plot(lambda x:2*x , x_range=[-3.5,3.5] , color=BLUE)
        value = MathTex(r"??" , color=GOLD).scale(0.8).next_to(slope_text_new , direction=RIGHT , buff=0.15)

        self.play(ReplacementTransform(line2 , line) , ReplacementTransform(slope_value_number , value))



        self.wait()


class Scene4(Scene):
    def construct(self):
        # self.add(NumberPlane())
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        )
        line = ax.plot(lambda x:2*x , x_range=[-3.5,3.5] , color=BLUE)
        slope_text = Text("Slope = " , color=GREEN).move_to([-5,3,0]).scale(0.63)
        value = MathTex(r"[-\infty , \infty]" , color=GOLD).scale(0.8).next_to(slope_text , direction=RIGHT , buff=0.15)
        slope_text_new = Text("m = " , color=GREEN).scale(0.63).next_to(value , LEFT , buff=0.15)
        value = MathTex(r"??" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        xaxis_clockwise_angle = ArcBetweenPoints(start=[0.5,0,0] , end=[0.3,0.6,0] , stroke_color=GOLD , stroke_width = 1.5)
        yaxis_angle = ArcBetweenPoints(start=[0,0.625,0] , end=[0.3,0.6,0] , stroke_color=RED , stroke_width = 1.5 , radius=-0.5)
        xaxis_anti_angle = ArcBetweenPoints(start=[-0.5,0,0] , end=[0.3,0.6,0] , stroke_color=RED , stroke_width = 1.5 , radius=-0.7)
        theta_text = MathTex(r"\theta" , color=GOLD).scale(0.6).move_to([0.3,0.25,0])
        value2 = MathTex(r"tan(\theta)" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        value3 = MathTex(r"tan(63.435^{\circ})" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        value4 = MathTex(r"2" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        value5 = MathTex(r"??" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        triangle_side = Line(start=[1,2,0] , end=[1,0,0] , buff=0 , color=GREEN)
        value6 = MathTex(r"\frac{Perpendicular}{Base}" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        value7 = MathTex(r"\frac{4}{Base}" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        value8 = MathTex(r"\frac{4}{2}" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        value9 = MathTex(r"2" , color=GOLD).scale(0.8).next_to(slope_text_new , RIGHT , buff=0.15)
        

        self.add(ax)
        self.add(line)
        self.add(slope_text_new)
        self.add(value)

        self.wait()
        self.play(Indicate(ax.get_axis(0) , scale_factor=1.05))
        self.play(Create(xaxis_clockwise_angle))
        self.play(Create(yaxis_angle) , FadeOut(xaxis_clockwise_angle))
        self.play(Create(xaxis_anti_angle) , FadeOut(yaxis_angle))

        self.play(Create(xaxis_clockwise_angle) , FadeOut(xaxis_anti_angle))
        self.play(Write(theta_text))

        self.play(TransformMatchingTex(value, value2))
        self.play(TransformMatchingTex(value2, value3))
        self.play(Transform(value3, value4))

        self.play(Transform(value3 , value5))
        self.play(Create(triangle_side))

        self.play(Transform(value3 , value2))
        self.play(Transform(value3 , value6))

        # self.play(Indicate(triangle_side))
        brace = Brace(triangle_side , direction=RIGHT , buff=0.2 , sharpness=0.9).scale(0.9)
        brace_value = MathTex(r"4").scale(0.67).next_to(brace , RIGHT , buff=0.15)
        self.play(FadeIn(brace))
        self.play(FadeIn(brace_value))
        self.play(TransformMatchingTex(value3 , value7))
        self.play(FadeOut(brace) , FadeOut(brace_value))

        self.play(TransformMatchingTex(value7 , value8))
        self.play(TransformMatchingTex(value8 , value9))



        self.wait()

        self.play(FadeOut(line) , FadeOut(slope_text_new) , FadeOut(value9) , FadeOut(triangle_side) , FadeOut(xaxis_clockwise_angle) , FadeOut(theta_text))

        self.wait()


class Scene5(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        )
        line = ax.plot(lambda x:-0.5*x , x_range=[-6.5,6.5] , color=BLUE , stroke_width = 2)
        triangle_side = Line(start=[-3,1.5,0] , end=[-3,0,0] , buff=0 , color=GREEN , stroke_width = 2)
        xaxis_anti_angle = Sector(outer_radius=0.5 , inner_radius=0 , start_angle = 2.6779 , angle=0.4636 , fill_color=RED , fill_opacity=1)
        xaxis_clockwise_angle = Sector(outer_radius=0.5 , inner_radius=0 , start_angle = 2.6779 , angle=-2.6779 , fill_color=GOLD , fill_opacity=1)
        theta = MathTex(r"\theta" , color=RED).scale(0.6).move_to([-0.7,0.17,0])
        beta = MathTex(r"\beta" , color=GOLD).scale(0.6).move_to([0.5,0.5,0])
        slope_text = MathTex(r"tan(\theta) = " , r"\frac{Perpendiclar}{Base}").scale(0.75).move_to([2.15,2,0])
        slope_text[0].set_color(GREEN)
        slope_text[1].set_color(GOLD)

        slope_text2 = MathTex(r"tan(\theta) = " , r"\frac{3}{6}").scale(0.75).move_to([2.15,2,0])
        slope_text2[0].set_color(GREEN)
        slope_text2[1].set_color(GOLD)

        slope_text3 = MathTex(r"tan(\theta) = " , r"0.5").scale(0.75).move_to([2.15,2,0])
        slope_text3[0].set_color(GREEN)
        slope_text3[1].set_color(GOLD)

        slope_text4 = MathTex(r"Slope(m) = " , r"0.5").scale(0.75).move_to([2.15,2,0])
        slope_text4[0].set_color(GREEN)
        slope_text4[1].set_color(GOLD)

        slope_text5 = MathTex(r"Slope(m) = " , r"tan(\beta)").scale(0.75).move_to([2.15,2,0])
        slope_text5[0].set_color(GREEN)
        slope_text5[1].set_color(GOLD)

        slope_text6 = MathTex(r"Slope(m) = " , r"tan(153.435^{\circ})").scale(0.75).move_to([2.15,2,0])
        slope_text6[0].set_color(GREEN)
        slope_text6[1].set_color(GOLD)

        slope_text7 = MathTex(r"Slope(m) = " , r"-0.5").scale(0.75).move_to([2.15,2,0])
        slope_text7[0].set_color(GREEN)
        slope_text7[1].set_color(GOLD)

        qmark = MathTex(r"?" , color=YELLOW).scale(0.8).next_to(slope_text4 , RIGHT)
        qmark2 = MathTex(r"\times" , color=RED).scale(0.8).next_to(slope_text4 , RIGHT)





        self.add(ax)

        self.wait()
        self.play(Create(line))
        self.play(Create(triangle_side))
        self.play(Create(xaxis_anti_angle) , Write(theta))

        self.play(Write(slope_text))

        brace = Brace(triangle_side , direction=LEFT , buff=0.2 , sharpness=0.9).scale(0.9)
        brace_value = MathTex(r"3").scale(0.67).next_to(brace , LEFT , buff=0.15)
        self.play(FadeIn(brace))
        self.play(FadeIn(brace_value))

        self.play(TransformMatchingTex(slope_text , slope_text2))

        self.play(FadeOut(brace) , FadeOut(brace_value))
        self.play(TransformMatchingTex(slope_text2 , slope_text3))
        self.play(TransformMatchingTex(slope_text3 , slope_text4))

        self.play(FadeIn(qmark))
        self.play(Transform(qmark , qmark2))
        
        self.play(Create(xaxis_clockwise_angle))
        self.play(Indicate(xaxis_anti_angle))
        self.play(Indicate(xaxis_clockwise_angle))

        slope_text3.move_to([-3,-1,0])
        thetaeqn = MathTex(r"\theta" , r"=" , r"tan^{-1}(0.5)").scale(0.75).next_to(slope_text3 , DOWN)
        thetaeqn[0].set_color(RED)
        thetaeqn[2].set_color(GOLD)

        thetaeqn2 = MathTex(r"\theta" , r"=" , r"26.565^{\circ}").scale(0.75).next_to(thetaeqn , DOWN)
        thetaeqn2[0].set_color(RED)
        thetaeqn2[2].set_color(GOLD)
        thetaeqns = VGroup(slope_text3 , thetaeqn , thetaeqn2)
        animations = [
            thetaeqns.animate.shift(LEFT * 2.5)
        ]


        betaeqn = MathTex(r"\theta" , r"+" , r"\beta" , r"=180^{\circ}").scale(0.75).move_to([-2,-1,0])
        betaeqn[0].set_color(RED)
        betaeqn[2].set_color(GOLD)
        betaeqn[3].set_color(GOLD)


        betaeqn2 = MathTex(r"\beta" , r"=" , r"153.435^{\circ}").scale(0.75).next_to(betaeqn , DOWN)
        betaeqn2[0].set_color(GOLD)
        betaeqn2[2].set_color(GOLD)

        self.play(Write(slope_text3))
        self.play(FadeIn(thetaeqn))
        self.play(FadeIn(thetaeqn2))

        self.play(Write(beta))
        self.play(AnimationGroup(*animations))

        self.play(Write(betaeqn) , thetaeqns.animate.scale(0.8))
        self.play(FadeIn(betaeqn2))

        self.play(TransformMatchingTex(slope_text4 , slope_text5) , FadeOut(qmark))
        self.play(TransformMatchingTex(slope_text5 , slope_text6))
        self.play(TransformMatchingTex(slope_text6 , slope_text7))


        self.play(
            FadeOut(*[triangle_side , betaeqn , betaeqn2 , beta , thetaeqns , theta , xaxis_anti_angle , xaxis_clockwise_angle])
        )
        self.wait()


class Scene6(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        )

        ax2 = Axes(
            x_range=[-5,5,0.5],
            y_range=[-3.5,3.5,0.5],
            x_length=20,
            y_length=14,
            axis_config={
                "include_numbers": True,
                "font_size":16,
                "line_to_number_buff":0.15,
                "decimal_number_config":{"num_decimal_places": 0},
                "numbers_to_exclude":[0.5,-0.5,1.5,-1.5,2.5,-2.5,3.5,-3.5]
            }
        )
        line = ax.plot(lambda x:-0.5*x , x_range=[-6.5,6.5] , color=BLUE , stroke_width = 2)
        line2 = ax2.plot(lambda x:-0.5*x , x_range=[-6.5,6.5] , color=BLUE , stroke_width = 2)
        slope_text = MathTex(r"Slope(m) = " , r"-0.5").scale(0.75).move_to([2.15,2,0])
        slope_text[0].set_color(GREEN)
        slope_text[1].set_color(GOLD)

        point = Dot(color=GREEN)
        l1 = Line(start=[0,0,0] , end=[2,0,0],buff=0 , color=RED)
        l2 = Line(start=[2,0,0] , end=[2,-1,0],buff=0 , color=RED)
        l3 = Line(start=[2,-1,0] , end=[4,-1,0],buff=0 , color=RED)
        l4 = Line(start=[4,-1,0] , end=[4,-2,0],buff=0 , color=RED)

        b1 = Brace(l1 , UP , sharpness=1 , buff=0.1)
        v1 = Text("1" , color=RED).scale(0.5).next_to(b1 , UP , buff=0.1)
        b2 = Brace(l2 , RIGHT , sharpness=0.5 , buff=0.1)
        v2 = Text("0.5" , color=RED).scale(0.5).next_to(b2 , RIGHT , buff=0.1)

        b3 = Brace(l3 , UP , sharpness=1 , buff=0.1)
        v3 = Text("1" , color=RED).scale(0.5).next_to(b3 , UP , buff=0.1)
        b4 = Brace(l4 , RIGHT , sharpness=0.5 , buff=0.1)
        v4 = Text("0.5" , color=RED).scale(0.5).next_to(b4 , RIGHT , buff=0.1)

        
        self.add(*[ax , line , slope_text])
        self.wait()

        self.play(TransformMatchingShapes(ax , ax2) , Transform(line , line2) , rate_func = linear)
        self.play(FadeIn(point))
        self.play(point.animate.shift(RIGHT * 2), Create(l1) , rate_func = linear , run_time = 1.5)
        self.play(FadeIn(*[b1,v1]))
        self.wait()
        self.play(point.animate.shift(DOWN), Create(l2) , rate_func = linear , run_time = 1)
        self.play(FadeIn(*[b2,v2]))
        self.wait()

        self.play(FadeOut(*[b1,v1,b2,v2]))
        self.play(point.animate.shift(RIGHT * 2), Create(l3) , rate_func = linear , run_time = 1.5)
        self.play(FadeIn(*[b3,v3]))
        self.wait()
        self.play(point.animate.shift(DOWN), Create(l4) , rate_func = linear , run_time = 1)
        self.play(FadeIn(*[b4,v4]))
        self.wait()

        self.play(Indicate(slope_text))
        self.play(FadeOut(*[b3,v3,b4,v4]))
        self.wait()

        self.play(FadeOut(*[ax2 , line , l1,l2,l3,l4,slope_text , point]))

        self.wait()


class Scene7(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        )
        line = ax.plot(lambda x:2*x , x_range=[-3.5,3.5] , color=BLUE , stroke_width = 2)

        point = Dot([0.5,1,0] , color=GREEN)
        l1 = Line(start=[0.5,1,0] , end=[1,1,0] , buff=0 , color=RED , stroke_width=2)
        l2 = Line(start=[1,1,0] , end=[1,2,0] , buff=0 , color=RED , stroke_width=2)
        slope_text = MathTex(r"Slope =", r"2" , color=GREEN).move_to([-2,2.5,0]).scale(0.7)
        slope_text[1].set_color(GOLD)

        self.play(FadeIn(ax) , Create(line))
        self.play(FadeIn(point))
        self.play(point.animate.shift(RIGHT * 0.5) , Create(l1) , rate_func = linear , run_time = 0.5)
        self.wait()
        self.play(point.animate.shift(UP * 1) , Create(l2) , rate_func = linear , run_time = 1)
        self.play(Write(slope_text))

        self.wait()


class Scene8(Scene):
    def construct(self):
        # self.add(NumberPlane())
        number_line = NumberLine(
            x_range=[0,6,1],
            length=6,
            rotation=PI/2,
            include_numbers=True,
            font_size=16,
            line_to_number_buff=0.15,
            label_direction=LEFT
        ).shift(UP * 0.25)
        numberline_label = Text("Distance (cm)").scale(0.3).next_to(number_line , UP , buff=0.1).shift(RIGHT * 0.6)
        time = ValueTracker(0.00)
        time_text = Text("Time: " , color=BLUE).scale(0.5).move_to([3.5,3,0])
        time_value = always_redraw(lambda: MathTex(f"{round(time.get_value() , 2)} s").scale(0.7).next_to(time_text , RIGHT))
        antline = Line(start=[0,-3,0] , end=[0,1,0] , buff = 0, color=BLUE).shift(UP * 0.25)

        ax = Axes(
            x_range=[0,9,1],
            y_range=[0,6,1],
            x_length=9,
            y_length=6,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        ).shift(UP * 0.25)

        labels = ax.get_axis_labels(
            Text("Time (Second)").scale(0.3), Text("Distance (cm)").scale(0.3)
        )
        antline2 = ax.plot(lambda x:0.5*x, x_range=[0,8] , color=BLUE)

        ant = ImageMobject('./ant.png').scale(0.1)

        self.play(FadeIn(ant))
        self.play(FadeIn(number_line) , Write(numberline_label) , ant.animate.shift(DOWN * 2.75))
        self.play(Write(time_text) , Write(time_value))
        self.wait()

        self.play(ant.animate.shift(UP * 4) , time.animate.set_value(8), Create(antline) , rate_func = linear , run_time = 8) ###8
        self.wait()
        self.play(TransformMatchingShapes(number_line , ax), TransformMatchingShapes(numberline_label , labels[1]), TransformMatchingShapes(time_text , labels[0]) , FadeOut(time_value) , FadeOut(ant) , Transform(antline , antline2))


        self.wait()

class Scene9(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0,9,1],
            y_range=[0,6,1],
            x_length=9,
            y_length=6,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        ).shift(UP * 0.25).add_coordinates()

        labels = ax.get_axis_labels(
            Text("Time (Second)").scale(0.3), Text("Distance (cm)").scale(0.3)
        )
        antline = ax.plot(lambda x:0.5*x, x_range=[0,8] , color=BLUE)
        antlin2 = ax.plot(lambda x:3*x, x_range=[0,2] , color=BLUE)
        point1 = Dot(ax.coords_to_point(2, 1), color=GREEN)
        lines1 = ax.get_lines_to_point(ax.c2p(2,1))

        point2 = Dot(ax.coords_to_point(4, 2), color=GREEN)
        lines2 = ax.get_lines_to_point(ax.c2p(4,2))

        point3 = Dot(ax.coords_to_point(6, 3), color=GREEN)
        lines3 = ax.get_lines_to_point(ax.c2p(6,3))

        point4 = Dot(ax.coords_to_point(8, 4), color=GREEN)
        lines4 = ax.get_lines_to_point(ax.c2p(8,4))

        travellingpoint = Dot(ax.coords_to_point(0, 0), color=RED , radius=0.05)
        l1 = Line(start=ax.coords_to_point(0, 0) , end=ax.coords_to_point(1, 0) , buff=0 , color = RED , stroke_width=1.5)
        l2 = Line(start=ax.coords_to_point(1, 0) , end=ax.coords_to_point(1, 0.5) , buff=0 , color = RED , stroke_width=1.5)
        l3 = Line(start=ax.coords_to_point(1, 0.5) , end=ax.coords_to_point(2, 0.5) , buff=0 , color = RED , stroke_width=1.5)
        l4 = Line(start=ax.coords_to_point(2, 0.5) , end=ax.coords_to_point(2, 1) , buff=0 , color = RED , stroke_width=1.5)


        self.add(*[ax , labels , antline])
        self.wait()
        self.play(FadeIn(*[point1 , lines1]))
        self.play(FadeIn(*[point2 , lines2]))
        self.play(FadeIn(*[point3 , lines3]))
        self.play(FadeIn(*[point4 , lines4]))

        self.play(FadeIn(travellingpoint))
        self.play(Create(l1) , travellingpoint.animate.shift(RIGHT))
        self.play(Create(l2), travellingpoint.animate.shift(UP * 0.5))
        self.play(Create(l3), travellingpoint.animate.shift(RIGHT))
        self.play(Create(l4), travellingpoint.animate.shift(UP * 0.5))

        self.wait(2.5)
        self.play(Transform(antline , antlin2) , FadeOut(*[point1 , point2 , point3 , point4 , lines1 , lines2 , lines3 , lines4 , l1 , l2 , l3 , l4 , travellingpoint]))
        self.wait()

        travelling_point_x = ValueTracker(0.5)
        travellingpoint = always_redraw(lambda: Dot(ax.coords_to_point(travelling_point_x.get_value(),1.5), color=RED , radius=0.05) )

        p1 = always_redraw(lambda: Dot(ax.coords_to_point(0.5,1.5), color=RED , radius=0.05) )
        p2 = always_redraw(lambda: Dot(ax.coords_to_point(travelling_point_x.get_value(),travelling_point_x.get_value()*3), color=RED , radius=0.05) )
        l1 = always_redraw(lambda: Line(start=[ax.coords_to_point(0.5,1.5)] , end=[ax.coords_to_point(travelling_point_x.get_value(),1.5)] , buff=0 , stroke_width = 1.5 , color=RED) )
        l2 = always_redraw(lambda: Line(start=[ax.coords_to_point(travelling_point_x.get_value(),1.5)] , end=[ax.coords_to_point(travelling_point_x.get_value(),travelling_point_x.get_value()*3)] , buff=0 , stroke_width = 1.5 , color=RED) )

        self.play(FadeIn(*[travellingpoint,l1,l2 , p1, p2]))

        self.play(travelling_point_x.animate.set_value(1.5) , run_time=2)
        self.play(Indicate(labels[1]))
        self.play(Indicate(labels[0]))
        self.wait()
        self.play(FadeOut(*[ax , antline, labels, l1,l2,p1,p2,travellingpoint]))


class Scene10(Scene):
    def construct(self):
        title = Text("One last thing!", color=BLUE).scale(0.7)
        ax = Axes(
            x_range=[0,6,1],
            y_range=[0,5,1],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True , "font_size":16 , "line_to_number_buff":0.15,},
        ).add_coordinates()
        apoint = Dot(ax.coords_to_point(1,1), color=GREEN , radius=0.05)
        bpoint = Dot(ax.coords_to_point(3,4), color=GREEN , radius=0.05)
        atext = MathTex(r"A(1,1)" , color=GREEN).scale(0.5).next_to(apoint , DOWN , buff=0.1)
        btext = MathTex(r"B(3,4)" , color=GREEN).scale(0.5).next_to(bpoint , RIGHT , buff=0.1)
        ab = Line(start=apoint.get_center() , end=bpoint.get_center() , buff = 0, color=BLUE, stroke_width=1.5)
        l1 = Line(start=apoint.get_center() , end=bpoint.get_center() + DOWN*3 , buff = 0, color=BLUE, stroke_width=1.5)
        l2 = Line(start=bpoint.get_center() , end=bpoint.get_center() + DOWN*3 , buff = 0, color=BLUE, stroke_width=1.5)
        slopetext = MathTex("Slope (m) " , color=GOLD).scale(0.6).move_to([2.5,1,0])
        slopetext1 = MathTex(r" = \frac{3}{2}" , color=GOLD).scale(0.6).next_to(slopetext , RIGHT)
        slopetext2 = MathTex("= 1.5" , color=GOLD).scale(0.6).align_to(slopetext1 , LEFT).shift(UP * 0.35)

        self.wait()
        self.play(Write(title))
        self.play(title.animate.to_edge(UP) , Create(ax))
        self.play(FadeIn(*[apoint , atext]))
        self.play(FadeIn(*[bpoint , btext]))
        self.play(Create(ab))
        self.play(Create(l1) , Create(l2))
        self.play(Write(slopetext))
        self.play(Write(slopetext1))
        self.play(Write(slopetext2))
        self.play(Flash(apoint, run_time=1))
        self.play(Flash(bpoint, run_time=1))
        self.play(Wiggle(l2))
        self.play(Wiggle(l1))
        
        b1 = Brace(l2 , RIGHT , sharpness=0.8 , buff=0.1)
        b2 = Brace(l1 , DOWN , sharpness=0.8 , buff=0.1)
        v1 = Text("3").scale(0.4).next_to(b1 , RIGHT , buff=0.1)
        v2 = Text("2").scale(0.4).next_to(b2 , DOWN , buff=0.1)
        self.play(FadeIn(*[b1,v1]))
        self.play(FadeIn(*[b2,v2]))
        self.wait()
        self.play(FadeOut(*[ax , title , ab , apoint , bpoint , atext, btext , b1,b2,v1,v2 , slopetext , slopetext1 , slopetext2 , l1 , l2]))


        self.wait()