import os
from distutils.dir_util import mkpath
from lxml.etree import parse, SubElement, tostring

# Path to the experiment template XML document.
TEMPLATE_PATH = 'api/experiment-template.xml'


class Experiment(object):
    """
    Container for the properties necessary for a BehaviourSpace experiment.
    """

    def __init__(self, params=None, metrics=None, steps=100, name='Experiment'):
        self.params = params or {}
        self.metrics = metrics or []
        self.steps = steps
        self.name = name


    def add_metric(self, formula=None, color=None):
        """
        Adds a metric to the experiment.
        """
        if formula:
            self.metrics.append(formula)
        elif color:
            self.metrics.append('count patches with [pcolor = %s]' % color)
        else:
            raise Exception('Unable to create metric from: %s' % locals())
        return self


    def to_xml_tree(self):
        """
        Constructs a BehaviourSpace-compatible ElementTree from the Experiment
        properties.
        """
        tree = parse(TEMPLATE_PATH)
        exp_node = tree.getroot().find('experiment')
        exp_node.set('name', self.name)
        exp_node.find('timeLimit').set('steps', str(self.steps))

        for metric in self.metrics:
            SubElement(exp_node, 'metric').text = metric

        for name, value in self.params.items():
            param_node = SubElement(exp_node, 'enumeratedValueSet',
                                    variable=name)
            SubElement(param_node, 'value', value=str(value))

        return tree

    def to_xml(self):
        """
        Writes the experiment to a NetLogo BehaviourSpace-compatible XML
        document.
        """
        header = '''<?xml version="1.0" encoding="us-ascii"?>
<!DOCTYPE experiments SYSTEM "behaviorspace.dtd">\n'''
        return header + tostring(self.to_xml_tree().getroot(), encoding="utf-8")

    def write_xml(self, filename):
        """
        Writes the experiment details to the given file. Creates the destination
        directory if it doesn't exist.
        """
        # Ensure the output file exists.
        mkpath(os.path.dirname(filename))
        self.to_xml_tree().write(filename)
