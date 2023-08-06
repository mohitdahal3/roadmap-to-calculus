from manim import *
# from manim_imports_ext import *
from Derivatives import LineThroughPoints, positionFunction , velocityFunction


def velocityFunctionIntegral(t):
    return 5 * t * (5-t)

class Scene1(Scene):
    def construct(self):
        title = Text("Integrals" , color=BLUE).scale(0.85)
        subtitle = Text("\"Anti-Derivatives\"" , color=YELLOW).scale(0.5).shift(DOWN * 0.35)
        box = Rectangle(height=9 , width=16).scale(0.893).scale(0.75)


##########################################################################

        axes = Axes(
        x_range=[-1 , 6 , 1],
        x_length=7,
        y_range=[-10 , 60 , 10],
        y_length=7,
        axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                        'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Distance(m)" , color=RED).scale(0.5)
        )
        positionCurve = axes.plot(positionFunction , x_range=[0 , 5] , color=RED , stroke_width=3.35)
        soft = MathTex(r"s(" , r"t" , r")" , color= RED).scale(0.49).move_to(axes.coords_to_point(4.8 , 52))
        soft[1].set_color(WHITE)

        velocityCurve = axes.plot(velocityFunction , x_range=[0 , 5] , color=BLUE , stroke_width=3.35)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(4.7 , 2))
        voft[1].set_color(WHITE)



        derstuff = VGroup(axes , labels , positionCurve , soft , velocityCurve , voft).scale(0.75)

        time = ValueTracker(2.5)
        verticalLine = always_redraw(lambda: Line(start=axes.coords_to_point(time.get_value() , 0), end=axes.coords_to_point(time.get_value() , positionFunction(time.get_value())) , stroke_width=2))
        pointoncurve = always_redraw(lambda: Dot(axes.coords_to_point(time.get_value() , positionFunction(time.get_value())) , radius=0.07).scale(0.75))



##########################################################################

        self.play(Write(title))
        self.play(title.animate.shift(UP * 0.4) , Write(subtitle))
        self.play(FadeOut(title , subtitle) , Create(box))
        self.play(AnimationGroup(FadeIn(axes, labels) , Create(positionCurve , rate_func = linear) , Write(soft) , lag_ratio=0.65))
        self.play(AnimationGroup(Create(verticalLine) , FadeIn(pointoncurve) , lag_ratio=0.9))
        self.play(time.animate.set_value(4.5) , run_time = 2)
        self.play(time.animate.set_value(0) , run_time = 2.8)


        tangent = always_redraw(lambda: LineThroughPoints(point1=axes.coords_to_point(time.get_value() , positionFunction(time.get_value())) , point2=axes.coords_to_point(time.get_value() + 0.001 , positionFunction(time.get_value() + 0.001)) , line_length=3 , stroke_width=2 , color=GREEN))


        self.play(Create(tangent))
        self.play(time.animate.set_value(5), Create(velocityCurve) ,rate_func=linear, run_time = 4)
        self.wait(0.5)

        self.play(FadeOut(tangent , pointoncurve , verticalLine))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class Scene2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1 , 6 , 1],
            x_length=10.5,
            y_range=[0 , 40 , 10],
            y_length=6,
            axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                            'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Velocity(m/s)" , color=BLUE).scale(0.5)
        )
        velocityCurve = axes.plot(velocityFunctionIntegral , x_range=[0 , 5] , stroke_width = 2.2 , color=BLUE)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(5.3 , 2))
        voft[1].set_color(WHITE)

        veleqn = MathTex(r"v(" , r"t" , r") = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30))
        veleqn[1].set_color(WHITE)
        veleqn[3].set_color(WHITE)
        veleqn[5].set_color(WHITE)

        canvas = Rectangle(color=BLACK , height=10 , width=16 , stroke_width = 0).set_opacity(0.75)
        preveqn = MathTex(r"{d \; " , r"s(t)" ,  r"\over dt} = " , r"v(t)")
        preveqn[1].set_color(RED)
        preveqn[3].set_color(BLUE)

        preveqn2 = MathTex(r"{d \; " , r"s(t)" ,  r"\over dt} = " , r"5t(5-t)")
        preveqn2[1].set_color(RED)
        preveqn2[3].set_color(BLUE)

        powerRuleeqn = MathTex(r"\text{Power Rule: }" , r"{d \; " , r"(ax^{n})" ,  r"\over dx} = " , r"a \times nx^{n-1}").scale(0.7).to_corner(UR , buff = 0.65)
        powerRuleeqn.set_color_by_gradient(BLUE , GREEN)

        self.play(FadeIn(axes , labels) , run_time = 0.75)
        self.play(Create(velocityCurve) , rate_func = linear)
        self.play(AnimationGroup(Write(voft) , Write(veleqn) , lag_ratio=0.8))
        self.wait(0.5)
        self.play(AnimationGroup(FadeIn(canvas) , Write(preveqn) , lag_ratio=0.5) , rate_fun=linear , run_time = 3)
        self.play(Indicate(preveqn[1]))
        self.play(TransformMatchingTex(preveqn , preveqn2))
        self.wait()
        self.play(Write(powerRuleeqn))

        self.wait()
        self.play(FadeOut(powerRuleeqn , preveqn2) , FadeOut(canvas , run_time = 2 , rate_func = linear))

class Scene3(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1 , 6 , 1],
            x_length=10.5,
            y_range=[0 , 40 , 10],
            y_length=6,
            axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                            'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Velocity(m/s)" , color=BLUE).scale(0.5)
        )
        velocityCurve = axes.plot(velocityFunctionIntegral , x_range=[0 , 5] , stroke_width = 2.5 , color=BLUE)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(5.3 , 2))
        voft[1].set_color(WHITE)

        veleqn = MathTex(r"v(" , r"t" , r") = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30))
        veleqn[1].set_color(WHITE)
        veleqn[3].set_color(WHITE)
        veleqn[5].set_color(WHITE)

        dx_list = [0.5 , 0.25 , 0.125 , 0.0625 , 0.03125 , 1/64]

        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=velocityCurve,
                    x_range=[0 , 5],
                    stroke_width = 0,
                    stroke_color=WHITE,
                    dx=dx,
                ).set_opacity(0.7)
                    for dx in dx_list
            ]
        )

        # final_area = axes.get_area(graph=velocityCurve, x_range=[0,5] , opacity=0.7 , stroke_width=0)
        final_area = axes.get_riemann_rectangles(velocityCurve , x_range=[0 , 5] , dx = 1/512 , stroke_width=0).set_opacity(0.7)


        flat_curve = axes.plot(lambda x:0 , x_range=[0,5])
        flatrects = axes.get_riemann_rectangles(flat_curve , x_range=[0 , 5] , dx = dx_list[0])

        linearVelocityCurve = axes.plot(lambda x : 20 , x_range=[0 , 5] , stroke_width=2.5 , color=BLUE)

        linearVelocityEqn = MathTex(r"v(" , r"t" , r") = 20" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30)).align_to(veleqn , LEFT)
        linearVelocityEqn[1].set_color(WHITE)

        self.add(axes , labels , velocityCurve , voft , veleqn)

        nowarea = rectangles[0]
        anims = []
        for i in range(nowarea.__len__()):
            anims.append(ReplacementTransform(flatrects[i] , nowarea[i]))
        
        self.wait()
        self.play(AnimationGroup(*anims , lag_ratio=0.1) , run_time = 1 , rate_func=linear)

        self.wait(0.5)

        for i in range(1 , len(dx_list)):
            nextarea = rectangles[i]

            anims = []
            for i in range(nowarea.__len__()):
                anims.append(ReplacementTransform(nowarea[i] , VGroup(nextarea[i*2] , nextarea[(i*2) + 1]) ))
        
            self.play(AnimationGroup(*anims , lag_ratio=0.09) , run_time = 1 , rate_func = linear)

            nowarea = nextarea
            self.wait(0.4)



        # self.play(FadeTransform(nowarea , final_area))


        anims = []
        for i in range(nowarea.__len__()):
            anims.append(ReplacementTransform(nowarea[i] , VGroup(final_area[i*8] ,
                                                                   final_area[(i*8) + 1], 
                                                                   final_area[(i*8) + 2], 
                                                                   final_area[(i*8) + 3], 
                                                                   final_area[(i*8) + 4], 
                                                                   final_area[(i*8) + 5], 
                                                                   final_area[(i*8) + 6], 
                                                                   final_area[(i*8) + 7]) 
                                                                ))
        
        self.play(AnimationGroup(*anims , lag_ratio=0.005) , run_time = 1 , rate_func=linear)
        self.wait()
        self.play(Transform(velocityCurve , linearVelocityCurve) , FadeOut(final_area) , TransformMatchingTex(veleqn , linearVelocityEqn) , FadeOut(voft))
        self.wait()


class Scene4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1 , 6 , 1],
            x_length=10.5,
            y_range=[0 , 40 , 10],
            y_length=6,
            axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                            'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Velocity(m/s)" , color=BLUE).scale(0.5)
        )
        velocityCurve = axes.plot(velocityFunctionIntegral , x_range=[0 , 5] , stroke_width = 2.5 , color=BLUE)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(5.3 , 2))
        voft[1].set_color(WHITE)

        veleqn = MathTex(r"v(" , r"t" , r") = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30))
        veleqn[1].set_color(WHITE)
        veleqn[3].set_color(WHITE)
        veleqn[5].set_color(WHITE)

        linearVelocityCurve = axes.plot(lambda x : 20 , x_range=[0 , 5] , stroke_width=2.5 , color=BLUE)

        linearVelocityEqn = MathTex(r"v(" , r"t" , r") = 20" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30)).align_to(veleqn , LEFT)
        linearVelocityEqn[1].set_color(WHITE)

        velocityBrace = BraceBetweenPoints(point_1=axes.c2p(5.005 , 20) , point_2=axes.c2p(5.005,0) , direction=RIGHT , sharpness=2)
        vbracevalue = MathTex(r"20 \; m/s" , color=BLUE).scale(0.65).next_to(velocityBrace , RIGHT)

        timeBrace = BraceBetweenPoints(point_1=axes.c2p(0 , 20.005) , point_2=axes.c2p(5,20.005) , direction=UP , sharpness=2)
        tbracevalue = MathTex(r"5 \; \text{seconds}" , color=GOLD).scale(0.65).next_to(timeBrace , UP)

        rectangleArea = axes.get_area(linearVelocityCurve , x_range=[0 , 5] , stroke_width=0 , opacity=0.7 , color=GREEN)
        areaeqn = MathTex(r"20" , r"\times" , r"5" , r"\text{ meters}").scale(0.7).move_to(axes.c2p(2.5 , 10))
        areaeqn[0].set_color(BLUE)
        areaeqn[2].set_color(GOLD)


        canvas = Rectangle(color=BLACK , height=10 , width=16 , stroke_width = 0).set_opacity(0.8)
        thought = Tex("Distance as area?")

        hline = Line(start=axes.c2p(0 , 0) , end=axes.c2p(5.85,0) , color=YELLOW)
        vline = Line(start=axes.c2p(0 , 0) , end=axes.c2p(0,38.5) , color=YELLOW)


        self.add(axes , labels , linearVelocityCurve , linearVelocityEqn)
        self.wait()

        self.play(FadeIn(velocityBrace , scale=[1,0,1]) , Write(vbracevalue , rate_func = linear))
        self.play(FadeIn(timeBrace , scale=[0,1,1]) , Write(tbracevalue , rate_func = linear))

        self.play(FadeIn(rectangleArea , rate_func = smooth) , Write(areaeqn , rate_func = linear , run_time = 1.5))
        self.play(Indicate(rectangleArea , scale_factor=1))
        self.wait()


        self.play(AnimationGroup(FadeIn(canvas) , Write(thought) , lag_ratio=0.5) , rate_fun=linear , run_time = 2)
        self.wait()
        
        self.play(Unwrite(thought , run_time=0.8) , FadeOut(canvas , run_time = 1 , rate_func = linear))
        self.play(Create(hline))
        self.play(Indicate(labels[0]))
        self.play(Uncreate(hline) , run_time = 0.4)
        self.play(Create(vline))
        self.play(Indicate(labels[1]))
        self.play(FadeOut(vline))
        self.wait()
        self.play(ReplacementTransform(linearVelocityCurve , velocityCurve) , TransformMatchingTex(linearVelocityEqn , veleqn) , FadeOut(velocityBrace , timeBrace , vbracevalue , tbracevalue , rectangleArea , areaeqn), Write(voft) , run_time = 0.7)


        self.wait()


class Scene5(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1 , 6 , 1],
            x_length=10.5,
            y_range=[0 , 40 , 10],
            y_length=6,
            axis_config={'include_tip':True , 'include_numbers':True , 'font_size':20 ,'line_to_number_buff':0.17, 'tip_height':0.2 , 'tip_width':0.2,
                            'numbers_to_exclude':[-10 , -1]
                        }
        ).add_coordinates()
        labels = axes.get_axis_labels(
            Tex("Time(Sec)").scale(0.5), Tex("Velocity(m/s)" , color=BLUE).scale(0.5)
        )
        velocityCurve = axes.plot(velocityFunctionIntegral , x_range=[0 , 5] , stroke_width = 2.5 , color=BLUE)
        voft = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(5.3 , 2))
        voft[1].set_color(WHITE)

        veleqn = MathTex(r"v(" , r"t" , r") = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30))
        veleqn[1].set_color(WHITE)
        veleqn[3].set_color(WHITE)
        veleqn[5].set_color(WHITE)

        timetracker = ValueTracker(1)
        pointoncurve = always_redraw(lambda: Dot(axes.c2p(timetracker.get_value() , velocityFunctionIntegral(timetracker.get_value()) ) ))
        alwayschangingtext = always_redraw(lambda: Tex("Always Changing!" , color=YELLOW) )

        self.add(axes , velocityCurve , voft , veleqn , labels)        
        self.play(DrawBorderThenFill(pointoncurve))

        self.play(timetracker.animate.set_value(4.5) , run_time = 2)

        self.wait()