from manim import *
from Derivatives import LineThroughPoints, positionFunction , velocityFunction


def velocityFunctionIntegral(t):
    return 5 * t * (5-t)


def constantIntervalVelocityFunction(t):
    interval = int(t // 0.5)
    if interval >= 10:
        return 0
    return velocityFunctionIntegral(interval * 0.5)


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
            for j in range(nowarea.__len__()):
                anims.append(ReplacementTransform(nowarea[j] , VGroup(nextarea[j*2] , nextarea[(j*2) + 1]) ))
        
            self.play(AnimationGroup(*anims , lag_ratio=0.08) , run_time = 1 , rate_func = linear)

            nowarea = nextarea
            self.wait(0.5)



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
        
        self.play(AnimationGroup(*anims , lag_ratio=0.007) , run_time = 1 , rate_func=linear)
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

        def mySpecialArrow():
            a = axes.c2p(2.5 , 0)
            b = axes.c2p(timetracker.get_value() , velocityFunctionIntegral(timetracker.get_value()))
            abVector = [b[0] - a[0] , b[1] - a[1] , 0]
            abNormalized = normalize(abVector)
            scaleFactor = 0.8
            abNormalized = [value*scaleFactor for value in abNormalized]
            c = [b[0] + abNormalized[0] , b[1] + abNormalized[1] , 0]

            arrow = Arrow(LEFT*0.85 , RIGHT*0.85 , stroke_width=2 , max_tip_length_to_length_ratio=0.15).move_to(c).rotate(angle_of_vector(abVector) + PI)


            return arrow



        arrow = always_redraw(mySpecialArrow)
        alwaysChangingText = always_redraw(lambda: Tex("Always Changing!" , color=YELLOW).scale(0.7).next_to(arrow.get_start() , UP) )


        self.add(axes , velocityCurve , voft , veleqn , labels)
        self.play(DrawBorderThenFill(pointoncurve) , GrowArrow(arrow) , Write(alwaysChangingText) , run_time = 0.6)

        self.play(timetracker.animate.set_value(4.5) , run_time = 1.6)
        self.play(timetracker.animate.set_value(0.5) , run_time = 1.6)
        self.wait()
        self.play(FadeOut(alwaysChangingText , arrow , pointoncurve) , run_time = 0.5)

        self.wait()

class Scene6(Scene):
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


        velocityCurve2 = axes.plot(velocityFunctionIntegral , x_range=[0 , 5] , stroke_width = 2.5 , color=BLUE , stroke_opacity=0.5)
        voft2 = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(5.3 , 2))
        voft2[1].set_color(WHITE)
        voft2.set_opacity(0.5)

        veleqn2 = MathTex(r"v(" , r"t" , r") = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30))
        veleqn2[1].set_color(WHITE)
        veleqn2[3].set_color(WHITE)
        veleqn2[5].set_color(WHITE)
        veleqn2.set_opacity(0.5)



        constantIntervalVelocityFunctionGraph = VGroup(*[
            Line(
                start=axes.c2p(i * 0.5, constantIntervalVelocityFunction(i * 0.5)),
                end=axes.c2p((i + 1) * 0.5, constantIntervalVelocityFunction((i) * 0.5)),
                color=BLUE_B,
                stroke_width=2.5,
            )
            for i in range(10)
        ])

        dot = Dot(axes.c2p(0.5,0) , color=YELLOW , radius=DEFAULT_SMALL_DOT_RADIUS)
        line = constantIntervalVelocityFunctionGraph[0].copy().set_color(YELLOW)



        self.add(axes , labels , velocityCurve , voft , veleqn)
        self.wait(0.5)
        self.play(FadeTransform(velocityCurve , velocityCurve2) , FadeTransform(veleqn , veleqn2) , FadeTransform(voft , voft2) , run_time = 0.5)
        anims = [Create(constantIntervalVelocityFunctionGraph[i]) for i in range(constantIntervalVelocityFunctionGraph.__len__())]
        self.play(AnimationGroup(*anims , lag_ratio=0.3) , run_time = 1.385)
        self.wait()
        self.play(Create(line) , run_time = 0.8)
        self.wait(0.5)
        self.play(ReplacementTransform(line , dot) , run_time = 1/3)

        line = constantIntervalVelocityFunctionGraph[1].copy().set_color(YELLOW)
        dot2 = Dot(line.get_start() , color=YELLOW , radius = DEFAULT_SMALL_DOT_RADIUS)

        self.play(Transform(dot , dot2) , run_time = 1/3)
        self.play(ReplacementTransform(dot , line) , run_time = 1/3)


        self.wait(0.5)
        dot = Dot(line.get_end() , color=YELLOW , radius=DEFAULT_SMALL_DOT_RADIUS)
        self.play(ReplacementTransform(line , dot) , run_time = 1/3)

        line = constantIntervalVelocityFunctionGraph[2].copy().set_color(YELLOW)
        dot2 = Dot(line.get_start() , color=YELLOW , radius = DEFAULT_SMALL_DOT_RADIUS)

        self.play(Transform(dot , dot2) , run_time = 1/3)
        self.play(ReplacementTransform(dot , line) , run_time = 1/3)



        self.wait(0.5)
        dot = Dot(line.get_end() , color=YELLOW , radius=DEFAULT_SMALL_DOT_RADIUS)
        self.play(ReplacementTransform(line , dot) , run_time = 1/3)

        line = constantIntervalVelocityFunctionGraph[3].copy().set_color(YELLOW)
        dot2 = Dot(line.get_start() , color=YELLOW , radius = DEFAULT_SMALL_DOT_RADIUS)

        self.play(Transform(dot , dot2) , run_time = 1/3)
        self.play(ReplacementTransform(dot , line) , run_time = 1/3)



        self.wait(0.5)
        dot = Dot(line.get_end() , color=YELLOW , radius=DEFAULT_SMALL_DOT_RADIUS)
        self.play(ReplacementTransform(line , dot) , run_time = 1/3)

        line = constantIntervalVelocityFunctionGraph[4].copy().set_color(YELLOW)
        dot2 = Dot(line.get_start() , color=YELLOW , radius = DEFAULT_SMALL_DOT_RADIUS)

        self.play(Transform(dot , dot2) , run_time = 1/3)
        self.play(ReplacementTransform(dot , line) , run_time = 1/3)
        self.wait()



class Scene7(Scene):
    def construct(self):
        carImage = ImageMobject("./car.png").scale(0.04)
        line = Line(start=LEFT * 5.4 , end=RIGHT * 5.4 , stroke_width=2 , color=RED).next_to(carImage , DOWN , buff=0)
        carImage.shift(LEFT * 5.4)

        self.add(carImage , line)
        self.wait(0.7)
        self.play(carImage.animate.shift(RIGHT * 2.8) , run_time = 2.8 , rate_func = linear)
        self.play(carImage.animate.shift(RIGHT * 3.8) , run_time = 1.15 , rate_func = linear)
        self.play(carImage.animate.shift(RIGHT * 4.2) , run_time = 0.5 , rate_func = linear)
        self.wait(0.5)
        self.play(carImage.animate.shift(LEFT * 7) , run_time = 0)
        self.wait(0.5)
        self.play(carImage.animate.shift(RIGHT * 4) , run_time = 0)
        self.wait(0.5)
        self.play(carImage.animate.shift(LEFT * 6) , run_time = 0)
        self.wait()

class Scene8(Scene):
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


        velocityCurve2 = axes.plot(velocityFunctionIntegral , x_range=[0 , 5] , stroke_width = 2.5 , color=BLUE , stroke_opacity=0.5)
        voft2 = MathTex(r"v(" , r"t" , r")" , color= BLUE).scale(0.49).move_to(axes.coords_to_point(5.3 , 2))
        voft2[1].set_color(WHITE)
        voft2.set_opacity(0.5)

        veleqn2 = MathTex(r"v(" , r"t" , r") = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30))
        veleqn2[1].set_color(WHITE)
        veleqn2[3].set_color(WHITE)
        veleqn2[5].set_color(WHITE)
        veleqn2.set_opacity(0.5)

        constantIntervalVelocityFunctionGraph = VGroup(*[
            Line(
                start=axes.c2p(i * 0.5, constantIntervalVelocityFunction(i * 0.5)),
                end=axes.c2p((i + 1) * 0.5, constantIntervalVelocityFunction((i) * 0.5)),
                color=BLUE_B,
                stroke_width=2.5,
            )
            for i in range(10)
        ])

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

        final_area = axes.get_riemann_rectangles(velocityCurve , x_range=[0 , 5] , dx = 1/512 , stroke_width=0).set_opacity(0.7)


        flat_curve = axes.plot(lambda x:0 , x_range=[0,5])
        flatrects = axes.get_riemann_rectangles(flat_curve , x_range=[0 , 5] , dx = dx_list[0])

        vbrace = Brace(rectangles[0][1] , RIGHT)
        hbrace = Brace(rectangles[0][1] , UP)

        vbraceValue = Tex("11.25 m/s" , color=BLUE).scale(0.65).next_to(vbrace , RIGHT , buff=0.15)
        hbraceValue = Tex("0.5 s").scale(0.65).next_to(hbrace , UP , buff=0.15)

        self.add(axes , labels , velocityCurve2 , voft2 , veleqn2 , constantIntervalVelocityFunctionGraph)
        self.play(FadeIn(rectangles[0][1]))
        self.wait(0.5)
        self.play(GrowFromCenter(vbrace , run_time = 0.5) , Write(vbraceValue , rate_func = linear))
        self.wait(0.5)
        self.play(GrowFromCenter(hbrace , run_time = 0.5) , Write(hbraceValue , rate_func = linear))
        self.wait()


        nowarea = rectangles[0]
        anims = []
        for i in range(nowarea.__len__()):
            if (i == 1):
                continue
            anims.append(ReplacementTransform(flatrects[i] , nowarea[i]))
        
        self.wait()
        self.play(AnimationGroup(*anims , lag_ratio=0.1) , run_time = 0.9 , rate_func=linear)
        self.wait(1.5)
        VGroup(hbrace , vbrace , hbraceValue , vbraceValue).set_opacity(0.7)
        self.play(FadeOut(hbrace , vbrace , hbraceValue , vbraceValue , constantIntervalVelocityFunctionGraph) , FadeTransform(velocityCurve2 , velocityCurve) , FadeTransform(voft2 , voft) , FadeTransform(veleqn2 , veleqn))

        self.wait(0.5)

        for i in range(1 , len(dx_list)):
            nextarea = rectangles[i]

            anims = []
            for j in range(nowarea.__len__()):
                anims.append(ReplacementTransform(nowarea[j] , VGroup(nextarea[j*2] , nextarea[(j*2) + 1]) ))
        
            self.play(AnimationGroup(*anims , lag_ratio=0.08) , run_time = 1 , rate_func = linear)

            nowarea = nextarea
            self.wait(0.5)



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
        
        self.play(AnimationGroup(*anims , lag_ratio=0.007) , run_time = 1 , rate_func=linear)
        self.wait(2)


        newrectangles = axes.get_riemann_rectangles(
                    graph=velocityCurve,
                    x_range=[0 , 5],
                    stroke_width = 0.5,
                    stroke_color=BLACK,
                    dx=0.25,
                ).set_opacity(0.7)
        
        self.play(ReplacementTransform(final_area , newrectangles , run_time = 1, lag_ratio = 0.0003))

        self.wait()


class Scene9(Scene):
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

        rectangles = axes.get_riemann_rectangles(
                    graph=velocityCurve,
                    x_range=[0 , 5],
                    stroke_width = 0.5,
                    stroke_color=BLACK,
                    dx=0.25,
                ).set_opacity(0.7)
        
        ticks = VGroup()
        i = 0
        while (i <= 5):
            ticks.add(Line(start=axes.coords_to_point(i , 1) , end=axes.coords_to_point(i , -1) , stroke_width=2 , color=YELLOW))
            i += 0.25

        brace = Brace(rectangles[4] , DOWN , buff = SMALL_BUFF , sharpness=3)
        braceValue = MathTex(r"\Delta t").scale(0.5).next_to(brace , DOWN , buff=SMALL_BUFF)
        dtValue = MathTex(r"\Delta t" , r" = " , r"0.25").to_corner(UR , buff=0.7).scale(0.7)
        dtValue[2].set_color(YELLOW)
        downBrace = VGroup(brace , braceValue)

        lArrow = Arrow(axes.c2p(0.5,5) , axes.c2p(1,0) , stroke_width=2 , max_tip_length_to_length_ratio=0.2 , buff=0.08)
        ltext = Tex("t = 1" , color=YELLOW).scale(0.7).next_to(lArrow.get_start() , UP , buff=SMALL_BUFF)

        rArrow = Arrow(axes.c2p(1.75,5) , axes.c2p(1.25,0) , stroke_width=2 , max_tip_length_to_length_ratio=0.2 , buff=0.08)
        rtext = Tex("t = 1.25" , color=YELLOW).scale(0.7).next_to(rArrow.get_start() , UP , buff=SMALL_BUFF)


        leftHeight = Line(start = axes.c2p(1,0) , end = axes.c2p(1,20) , color=YELLOW , stroke_width=2)
        rightHeight = Line(start = axes.c2p(1.25,0) , end = axes.c2p(1.25,velocityFunctionIntegral(1.25)) , color=YELLOW , stroke_width=2)

        downWidth = DashedLine(start = leftHeight.get_end() , end = axes.c2p(0 , 20) , stroke_width=2)
        upWidth = DashedLine(start = rightHeight.get_end() , end = axes.c2p(0 , velocityFunctionIntegral(1.25)) , stroke_width=2)
        increasedVelocityText = Tex("23.437").scale(0.45).next_to(upWidth.get_end() , LEFT , buff=0.1)

        tEquals1toEqnarrow = Arrow(axes.c2p(3.5,25) , axes.c2p(4.2,29) , stroke_width=2 , max_tip_length_to_length_ratio=0.14 , buff=0)
        tEquals1toEqntext = Tex("t = 1" , color=YELLOW).scale(0.7).next_to(tEquals1toEqnarrow.get_start() , LEFT , buff=SMALL_BUFF)
        tEquals125toEqntext = Tex("t = 1.25" , color=YELLOW).scale(0.7).next_to(tEquals1toEqnarrow.get_start() , LEFT , buff=SMALL_BUFF)

        longerRectangle = axes.get_riemann_rectangles(
                    graph=axes.plot(lambda t:23.4375 , x_range=[0,5]),
                    x_range=[0 , 5],
                    stroke_width = 0.5,
                    stroke_color=BLACK,
                    dx=0.25,
                ).set_opacity(0.7)[4]

        answerArrow = Arrow(axes.c2p(1.75 , 17) , axes.c2p(1.125 , 17) , buff=0 , max_tip_length_to_length_ratio=0.16 , stroke_width=3)
        answerText = MathTex(r"20 m/s \times 0.25s = 5m").scale(0.7).next_to(answerArrow , RIGHT)
        errorTriangle = Polygon(axes.c2p(1,20) , axes.c2p(1.25 , 23.4375) , axes.c2p(1.25 , 20) , stroke_width=0.5 , color=RED , fill_color=RED , fill_opacity=0.7 , stroke_opacity=0.7)


        vbrace = Brace(rectangles[5] , LEFT , buff = SMALL_BUFF , sharpness=2)
        vbraceText = MathTex(r"v(t)").scale(0.7).next_to(vbrace , LEFT , buff=SMALL_BUFF)
        VbraceGroup = VGroup(vbrace , vbraceText)

        self.add(axes , labels , velocityCurve , voft , veleqn , rectangles)
        self.wait()

        anims = []
        for i in range(ticks.__len__()):
            anims.append(Create(ticks[i]))
        
        self.play(AnimationGroup(*anims , lag_ratio=0.35) , run_time = 0.55)
        self.wait()
        self.play(GrowFromCenter(brace) , Write(braceValue))
        self.wait()
        self.play(TransformFromCopy(braceValue , dtValue[0]))
        self.play(Write(VGroup(dtValue[1] , dtValue[2])))

        anims = []
        for i in range(rectangles.__len__()):
            if(i==4):
                continue
            anims.append(rectangles[i].animate.set_opacity(0.2))

        self.play(AnimationGroup(*anims , lag_ratio=0) , run_time = 0.65)
        self.wait(0.4)
        self.play(FadeIn(lArrow , ltext) , run_time = 0.3)
        self.wait(0.7)
        self.play(FadeIn(rArrow , rtext) , run_time = 0.3)
        self.wait()

        self.play(Create(leftHeight) , run_time = 1)
        self.play(Create(downWidth) , run_time = 0.7)

        self.wait(0.5)
        self.play(Create(rightHeight) , run_time = 1)
        self.play(Create(upWidth), Write(increasedVelocityText) , run_time = 0.7)

        self.play(TransformFromCopy(lArrow , tEquals1toEqnarrow) , TransformFromCopy(ltext , tEquals1toEqntext))
        self.wait(0.4)
        self.play(Transform(tEquals1toEqntext , tEquals125toEqntext) , run_time = 0.85)
        self.play(FadeOut(tEquals1toEqnarrow , tEquals1toEqntext))

        self.wait(2)



        self.play(Indicate(rectangles[4] , scale_factor=1))
        self.wait()
        self.play(Transform(rectangles[4] , longerRectangle) , rate_func = there_and_back , run_time = 2.4)

        otherclip = Text("Put the other clip")
        self.wait()
        self.add(otherclip)
        self.wait()
        self.remove(otherclip)
        self.wait()

        self.play(Uncreate(rightHeight) , FadeOut(upWidth , increasedVelocityText) , run_time = 0.6)
        self.wait(0.5)
        
        self.play(FadeIn(answerArrow , run_time = 0.7) , Write(answerText , rate_func=linear , run_time = 3))
        self.play(DrawBorderThenFill(errorTriangle))
        self.wait(0.5)
        self.play(FadeOut(errorTriangle))
        self.wait()
        self.play(FadeIn(VbraceGroup) , FadeOut(leftHeight , downWidth , answerArrow , answerText , lArrow , rArrow , ltext , rtext) , downBrace.animate.next_to(rectangles[5] , DOWN , buff=SMALL_BUFF) , rectangles[4].animate.set_opacity(0.2) , rectangles[5].animate.set_opacity(0.7))


        self.wait(0.5)
        for i in range(6 , 14):
            #I can probably refactor this line but it works! so who cares
            self.play(Transform(vbrace , Brace(rectangles[i] , LEFT , buff = SMALL_BUFF , sharpness=2)), Transform(vbraceText , MathTex(r"v(t)").scale(0.7).next_to(Brace(rectangles[i] , LEFT , buff = SMALL_BUFF , sharpness=2) , LEFT , buff=SMALL_BUFF)) ,downBrace.animate.next_to(rectangles[i] , DOWN , buff=SMALL_BUFF) , rectangles[i-1].animate.set_opacity(0.2) , rectangles[i].animate.set_opacity(0.7))
            self.wait(0.5)


        self.wait()


class Scene10(Scene):
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

        rectangles = axes.get_riemann_rectangles(
                    graph=velocityCurve,
                    x_range=[0 , 5],
                    stroke_width = 0.5,
                    stroke_color=BLACK,
                    dx=0.25,
                ).set_opacity(0.2)

        rectangles[13].set_opacity(0.7)

        ticks = VGroup()
        i = 0
        while (i <= 5):
            ticks.add(Line(start=axes.coords_to_point(i , 1) , end=axes.coords_to_point(i , -1) , stroke_width=2 , color=YELLOW))
            i += 0.25

        brace = Brace(rectangles[13] , DOWN , buff = SMALL_BUFF , sharpness=3)
        braceValue = MathTex(r"\Delta t").scale(0.5).next_to(brace , DOWN , buff=SMALL_BUFF)
        dtValue = MathTex(r"\Delta t" , r" = " , r"0.25").to_corner(UR , buff=0.7).scale(0.7)
        dtValue[2].set_color(YELLOW)
        downBrace = VGroup(brace , braceValue)

        vbrace = Brace(rectangles[13] , LEFT , buff = SMALL_BUFF , sharpness=2)
        vbraceText = MathTex(r"v(t)").scale(0.7).next_to(vbrace , LEFT , buff=SMALL_BUFF)
        VbraceGroup = VGroup(vbrace , vbraceText)

        sigma_sum_eqn = MathTex(r"\sum" , r"_{t=0}" , r"^{5}" , r"v(t) \; " , r"\Delta t").scale(0.7).to_corner(UR , buff=0.5).shift(LEFT * 0.5)
        integral_sum_eqn = MathTex(r"\int" , r"_{0}^{5} v(t) \; \Delta t").scale(0.7).to_corner(UR , buff=0.5).shift(LEFT * 0.5)
        del_t_box = DashedVMobject(Rectangle(stroke_width = 1 , color=YELLOW , height=0.5 , width=1), num_dashes=30).next_to(integral_sum_eqn , DOWN)
        del_t_to_0 = MathTex(r"\Delta t \to 0" , color=YELLOW).scale(0.55).move_to(del_t_box)
        integral_sum_eqn_with_dt = MathTex(r"\int" , r"_{0}^{5} v(t) \; dt").scale(0.7).to_corner(UR , buff=0.5).shift(LEFT * 0.5)
        dt_equals = Tex("dt = ").scale(0.55).next_to(del_t_box , LEFT , buff=0.15)

        canvas = Rectangle(color=BLACK , height=10 , width=16 , stroke_width = 0).set_opacity(0.8)
        centered_integral_sum_eqn_with_dt = MathTex(r"\int" , r"_{0}^{5} v(t) \; dt").scale(1.1)


        one_hard_problem_text = Tex("One hard problem" , color=BLUE).shift(UP * 1.5)
        another_hard_problem_text = Tex("Another hard problem").shift(DOWN * 1.5)
        into_arrow = Arrow(UP * 1.5 , DOWN * 1.5 , buff=MED_LARGE_BUFF , stroke_width=2 , max_tip_length_to_length_ratio=0.1)

        dont_worry_text = Tex("But don't worry!")

        self.add(axes , labels , ticks , downBrace , dtValue , velocityCurve , rectangles , veleqn , VbraceGroup , voft)
        self.wait()

        self.play(FadeOut(dtValue , run_time = 0.5) , Write(VGroup(sigma_sum_eqn[1] , sigma_sum_eqn[2]) , run_time = 2 , rate_func = linear))
        self.play(Write(sigma_sum_eqn[0]))
        self.play(TransformFromCopy(vbraceText , sigma_sum_eqn[3]))
        self.wait(0.3)
        self.play(TransformFromCopy(braceValue , sigma_sum_eqn[4]))

        self.wait(0.3)
        self.play(Indicate(sigma_sum_eqn[4]))
        self.wait(0.5)
        self.play(Circumscribe(sigma_sum_eqn[0] , Circle , time_width=4 , stroke_width=1 , run_time = 2) , Circumscribe(sigma_sum_eqn[2] , Circle , time_width=4 , stroke_width=1 , run_time = 2))

        self.play(sigma_sum_eqn.animate.shift(LEFT * 3.5).set_color(RED))
        self.play(Write(integral_sum_eqn) , run_time = 3 , rate_func = linear)

        self.wait(0.5)
        self.play(Indicate(integral_sum_eqn[0] , scale_factor=1.3))
        self.play(veleqn.animate.shift(DOWN * 0.25) , FadeIn(del_t_box) , Write(del_t_to_0))
        self.wait(0.5)
        self.play(TransformMatchingTex(integral_sum_eqn , integral_sum_eqn_with_dt) , FadeIn(dt_equals))

        self.wait(0.5)
        self.play(rectangles.animate.set_opacity(0.7), FadeOut(VbraceGroup , sigma_sum_eqn, ticks))




        dx_list = [0.5 , 0.125 , 0.0625 , 0.03125 , 1/64]
        rectangleslist = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=velocityCurve,
                    x_range=[0 , 5],
                    stroke_width = 0.01,
                    stroke_color=WHITE,
                    dx=dx,
                ).set_opacity(0.7)
                    for dx in dx_list
            ]
        )
        final_area = axes.get_riemann_rectangles(velocityCurve , x_range=[0 , 5] , dx = 1/512 , stroke_width=0).set_opacity(0.7)

        nowarea = rectangles

        self.wait(0.5)
        for i in range(1 , len(dx_list)):
            nextarea = rectangleslist[i]
            anims = []
            for j in range(nowarea.__len__()):
                # anims.append(AnimationGroup(ReplacementTransform(nowarea[j] , VGroup(nextarea[j*2] , nextarea[(j*2) + 1])) , Transform(brace , Brace(rectangleslist[j*2] , DOWN , buff = SMALL_BUFF , sharpness=3)) , lag_ratio=0))
                anims.append(ReplacementTransform(nowarea[j] , VGroup(nextarea[j*2] , nextarea[(j*2) + 1])) )
        
            self.play(AnimationGroup(*anims , lag_ratio=0.08 , rate_func=linear), brace.animate.scale([0.5 , 1 , 1]).shift(LEFT * (dx_list[i]/2)) , braceValue.animate.shift(LEFT * (dx_list[i]/2)) , run_time = 1)

            nowarea = nextarea
            self.wait(0.5)

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
        
        self.play(AnimationGroup(*anims , lag_ratio=0.007 , rate_func=linear), brace.animate.scale([0,1,1]).shift(LEFT * 1/512), braceValue.animate.shift(LEFT * 1/512) , run_time = 1)
        self.wait(1)
        # self.play(AnimationGroup(FadeIn(canvas , run_time = 0.3) , TransformFromCopy(integral_sum_eqn_with_dt , centered_integral_sum_eqn_with_dt , run_time = 1) , lag_ratio=0.9))
        self.play(FadeIn(canvas , run_time = 0.3))
        self.play(TransformFromCopy(integral_sum_eqn_with_dt , centered_integral_sum_eqn_with_dt , run_time = 1))
        self.wait(1)
        self.play(Write(one_hard_problem_text , run_time = 1) , FadeOut(centered_integral_sum_eqn_with_dt))
        self.play(GrowArrow(into_arrow))
        self.play(Write(another_hard_problem_text) , run_time = 1)
        self.wait(0.3)
        self.play(FadeOut(one_hard_problem_text , another_hard_problem_text , into_arrow , run_time = 0.4) , Write(dont_worry_text))
        self.wait()



class Scene11(Scene):
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

        veleqn = MathTex(r"v(" , r"t" , r")" , r" = 5" , r"t" , r"(5-" , r"t" , r")" , color=BLUE).scale(0.7).move_to(axes.c2p(5 , 30)).shift(DOWN * 0.25)
        veleqn[1].set_color(WHITE)
        veleqn[4].set_color(WHITE)
        veleqn[6].set_color(WHITE)

        timeTracker = ValueTracker(3.5)
        opacityTracker = ValueTracker(0.7)
        area_under_curve = always_redraw(lambda: axes.get_area(velocityCurve , x_range=[0 , timeTracker.get_value()] , opacity=opacityTracker.get_value() , stroke_width=0) )
        time_Tracker_line = always_redraw(lambda: Line(start=axes.c2p(timeTracker.get_value() , 0) , end=axes.c2p(timeTracker.get_value() , velocityFunctionIntegral(timeTracker.get_value())) , stroke_width=3 , color=YELLOW))
        little_triangle = always_redraw(lambda: Triangle(color = WHITE, fill_color=WHITE , fill_opacity=1 , stroke_width=0).scale(0.15).next_to(axes.c2p(timeTracker.get_value() , 0) , DOWN , buff=0))
        time_variable_text = always_redraw(lambda: MathTex("T").scale(0.6).next_to(axes.c2p(timeTracker.get_value() , -1.5) , DOWN , buff=SMALL_BUFF))

        integral_eqn = MathTex(r"s(" , r"T" , r")" , r" = " , r"\int" , r"_{0}^{T}" , r"v(" , r"t" , r")" , r"\; dt").scale(0.75).shift(UP * 2.6 + RIGHT*1.7)
        integral_eqn[0].set_color(RED)
        integral_eqn[2].set_color(RED)
        integral_eqn[6].set_color(BLUE)
        integral_eqn[8].set_color(BLUE)
        soft_arrow = Arrow(integral_eqn.get_corner(DL) , axes.c2p(1.6,23) , stroke_width=3 , max_tip_length_to_length_ratio=0.08 , buff=0)

        dtTracker = ValueTracker(0.15)
        small_area = always_redraw(lambda: axes.get_area(velocityCurve , x_range=[3.5 , 3.5 + dtTracker.get_value()] , opacity=0.6 , stroke_width=0) )

        downBrace = Brace(small_area , DOWN , sharpness=3 , buff=SMALL_BUFF)
        downBraceValue = MathTex(r"dT").scale(0.5).next_to(downBrace , DOWN , buff=SMALL_BUFF)

        smallDistanceText = MathTex(r"ds" , r"=" , r"v(T)" , r"\;dT").scale(0.7).move_to(axes.c2p(4.95 , 20))
        smallDistanceText[0].set_color(RED)

        smallDistanceTextAlt = MathTex(r"{ds" , r"\over dT}" , r"=" , r"v(T)").scale(0.7).move_to(axes.c2p(4.95 , 20)).align_to(smallDistanceText , LEFT)
        smallDistanceTextAlt[0].set_color(RED)


        smallDistanceArrow = Arrow(smallDistanceText.get_edge_center(LEFT) , axes.c2p(3.5 , 20) , stroke_width=3 , max_tip_length_to_length_ratio=0.1 , buff=SMALL_BUFF)

        vbrace = Brace(small_area , LEFT , buff = SMALL_BUFF)
        vbraceText = MathTex(r"v(T)").scale(0.75).next_to(vbrace , LEFT , buff=SMALL_BUFF)

        rectApproximation = Rectangle(color=YELLOW, fill_color=YELLOW , fill_opacity=0.7 , width=(small_area.get_corner(DR) - small_area.get_corner(DL))[0] , height=(small_area.get_corner(UL) - small_area.get_corner(DL))[1] , stroke_width=0.5).align_to(small_area , DL)


        self.add(axes , labels , voft , veleqn , velocityCurve)
        self.play(FadeIn(area_under_curve))
        self.play(DrawBorderThenFill(little_triangle) , Create(time_Tracker_line) , Write(time_variable_text))
        self.wait(0.5)
        self.play(timeTracker.animate.set_value(5))
        self.wait(0.5)
        self.play(timeTracker.animate.set_value(0) , run_time = 1.5)
        self.wait(0.5)
        self.play(timeTracker.animate.set_value(2))
        self.wait(0.5)
        self.play( Write(VGroup(integral_eqn[4] , integral_eqn[6] , integral_eqn[7] , integral_eqn[8] , integral_eqn[9])) , rate_func = linear , run_time = 2)
        self.wait(0.2)
        self.play(Write(integral_eqn[5]))
        self.wait()
        self.play(Write(VGroup(integral_eqn[0] , integral_eqn[1] , integral_eqn[2], integral_eqn[3])) , FadeIn(soft_arrow))
        self.play(FadeOut(soft_arrow))
        self.wait()
        self.play(timeTracker.animate.set_value(3.5))
        self.play(timeTracker.animate.set_value(3.65))

        self.play(opacityTracker.animate.set_value(0.25) , FadeIn(small_area) , ReplacementTransform(VGroup(little_triangle , time_variable_text) , VGroup(downBrace , downBraceValue)))
        self.wait()
        self.play(Write(smallDistanceText[0]))
        self.play(FadeIn(smallDistanceArrow))
        self.wait()
        self.play(GrowFromCenter(vbrace) , Write(vbraceText))
        self.wait()
        self.play(DrawBorderThenFill(rectApproximation) , run_time = 0.6)
        self.play(ReplacementTransform(smallDistanceArrow , smallDistanceText[1]) , TransformFromCopy(vbraceText , smallDistanceText[2]) , TransformFromCopy(downBraceValue , smallDistanceText[3]))
        self.play(FadeOut(rectApproximation , time_Tracker_line))
        self.wait()
        self.play(dtTracker.animate.set_value(0.01) , timeTracker.animate.set_value(3.51) , downBrace.animate.scale([0.01 , 1 , 1]).move_to(axes.c2p(3.505 , -1.9)), downBraceValue.animate.move_to(axes.c2p(3.505 , -3.6)) , run_time = 3, rate_func = linear )
        self.play(TransformMatchingShapes(smallDistanceText , smallDistanceTextAlt))
        self.wait()
        self.play(Indicate(VGroup(veleqn[0] , veleqn[1] , veleqn[2])) , Indicate(VGroup(integral_eqn[6] , integral_eqn[7] , integral_eqn[8])))
        self.wait(0.5)
        self.play(Indicate(VGroup(integral_eqn[0] , integral_eqn[1] , integral_eqn[2]))) 
        self.wait(0.5)
        self.play(Indicate( VGroup(smallDistanceTextAlt[0] , smallDistanceTextAlt[1]) ))
        self.wait(0.5)
        self.play(Indicate(smallDistanceTextAlt[3]))

        self.wait()

class Scene12(Scene):
    def construct(self):
        distanceEqn1 = MathTex("???" , color=RED).shift(LEFT * 1.5).scale(0.8)
        velEqn1 = MathTex(r"5t(5-t)" , color=BLUE).shift(RIGHT * 1.5).scale(0.8)


        upperArrow = CurvedArrow(LEFT * 1.5 + UP*0.5 , RIGHT * 1.5 + UP*0.5 , radius = -1.7).set_color(BLUE)
        lowerArrow = CurvedArrow(RIGHT * 1.5 + DOWN*0.5 , LEFT * 1.5 + DOWN*0.5 , radius = -1.7).set_color(RED)
        uptext = Tex("Derivative" , color=BLUE).scale(0.7).shift(UP * 2)
        downtext = Tex("Anti-Derivative" , color=RED).scale(0.7).shift(DOWN * 2)
        setup = VGroup(upperArrow , lowerArrow , uptext , downtext)
        setup2 = setup.copy()

        veleqn2 = MathTex(r"25t" , r"-5t^{2}" , color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn2Copy = MathTex(r"25t" , r"-5t^{2}" , color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn3_1 = MathTex(r"25t" , color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn3_2 = MathTex(r"-5t^2" , color=BLUE).to_corner(UR , buff=1).scale(0.8)

        distanceEqn2 = MathTex(r"t^{2}" , color=RED).shift(LEFT * 1.5).scale(0.8)
        distanceEqn3 = MathTex(r"25t^{2}" , color=RED).shift(LEFT * 1.5).scale(0.8)
        distanceEqn4 = MathTex(r"{25t^{2} \over 2}" , color=RED).shift(LEFT * 1.5).scale(0.75)
        distanceEqn5 = MathTex(r"t^{3}" , color=RED).shift(LEFT * 1.5).scale(0.8)
        distanceEqn6 = MathTex(r"-5t^{3}" , color=RED).shift(LEFT * 1.5).scale(0.8)
        distanceEqn7 = MathTex(r"-{5t^{3} \over 3}" , color=RED).shift(LEFT * 1.5).scale(0.75)

        distanceEqn8 = MathTex(r"{25t^{2} \over 2}" , r"-{5t^{3} \over 3}" , color=RED).shift(LEFT * 1.5).scale(0.75)

        veleqn4 = MathTex(r"2t", color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn5 = MathTex(r"25 \times 2t", color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn6 = MathTex(r"{25 \times 2t \over 2}", color=BLUE).shift(RIGHT * 1.5).scale(0.75)
        veleqn7 = MathTex(r"3t^{2}", color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn8 = MathTex(r"-5 \times 3t^{2}", color=BLUE).shift(RIGHT * 1.5).scale(0.8)
        veleqn9 = MathTex(r"-{5 \times 3t^{2} \over 3}", color=BLUE).shift(RIGHT * 1.5).scale(0.75)

        term1antiderivative = VGroup(setup , veleqn2[0] , distanceEqn4)

        self.add(distanceEqn1 , velEqn1)
        self.play(Create(upperArrow) , Create(lowerArrow) , run_time = 0.5)
        self.play(Write(uptext) , Write(downtext) , run_time = 1.5)
        self.play(TransformMatchingShapes(velEqn1 , veleqn2) , run_time = 1)
        # self.play(TransformMatchingShapes(veleqn2[0] , veleqn3_1) , TransformMatchingShapes(veleqn2[1] , veleqn3_2))
        self.play(veleqn2[0].animate.move_to(veleqn3_1) , veleqn2[1].animate.move_to(veleqn3_2))
        self.wait()
        self.play(veleqn2[0].animate.shift(DOWN + RIGHT))

        self.play(ReplacementTransform(distanceEqn1 , distanceEqn2))
        self.play(TransformFromCopy(distanceEqn2 , veleqn4 , path_arc = PI/1.5))

        self.play(TransformMatchingShapes(distanceEqn2 , distanceEqn3))
        self.play(ReplacementTransform(veleqn4 , veleqn5))

        self.play(TransformMatchingShapes(distanceEqn3 , distanceEqn4))
        self.play(ReplacementTransform(veleqn5 , veleqn6))

        self.play(FadeOut(veleqn6) , veleqn2[0].animate.move_to(veleqn3_1))
        self.add(setup2)

        distanceEqn1 = MathTex("???" , color=RED).shift(LEFT * 1.5).scale(0.8)
        self.play(term1antiderivative.animate.scale(0.6).to_corner(UL, buff=0.5))
        self.play(Write(distanceEqn1) , veleqn2[1].animate.move_to(RIGHT * 1.5))
        self.wait()
        self.play(veleqn2[1].animate.shift(DR))
        self.play(ReplacementTransform(distanceEqn1 , distanceEqn5))
        self.play(TransformFromCopy(distanceEqn5 , veleqn7 , path_arc = PI/1.5))

        self.play(TransformMatchingShapes(distanceEqn5 , distanceEqn6))
        self.play(TransformMatchingShapes(veleqn7 , veleqn8))

        self.play(TransformMatchingShapes(distanceEqn6 , distanceEqn7))
        self.play(TransformMatchingShapes(veleqn8 , veleqn9))
        self.play(FadeOut(veleqn9) , veleqn2[1].animate.move_to(RIGHT * 1.5))
        self.wait()

        self.play(FadeOut(setup) , ReplacementTransform(distanceEqn4 , distanceEqn8[0]) , TransformMatchingShapes(distanceEqn7 , distanceEqn8[1]) , TransformMatchingShapes(veleqn2[0] , veleqn2Copy[0]) , TransformMatchingShapes(veleqn2[1] , veleqn2Copy[1]))

        self.wait()