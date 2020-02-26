from elements.baseElement import BaseElement


class Element(BaseElement):

    def __init__(self, locator, selector, context):
        super().__init__(locator, selector, context)
