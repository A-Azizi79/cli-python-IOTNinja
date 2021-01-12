from base_controllers import ControllerGroup


class VerticalControllerGroup(ControllerGroup):

    def __init__(self, cg_id):
        super().__init__(cg_id)
        self.__define_type("verticalGroup")


class HorizontalControllerGroup(ControllerGroup):

    def __init__(self, cg_id):
        super().__init__(cg_id)
        self.__define_type("horizontalGroup")
