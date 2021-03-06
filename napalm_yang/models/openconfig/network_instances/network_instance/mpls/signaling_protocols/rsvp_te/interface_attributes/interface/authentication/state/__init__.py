
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/authentication/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information associated
with authentication
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enable','__authentication_key',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__authentication_key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'interface-attributes', u'interface', u'authentication', u'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/enable (boolean)

    YANG Description: Enables RSVP authentication on the node.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables RSVP authentication on the node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_authentication_key(self):
    """
    Getter method for authentication_key, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/authentication_key (string)

    YANG Description: authenticate RSVP signaling
messages
    """
    return self.__authentication_key
      
  def _set_authentication_key(self, v, load=False):
    """
    Setter method for authentication_key, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/authentication_key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_key() directly.

    YANG Description: authenticate RSVP signaling
messages
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)""",
        })

    self.__authentication_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_key(self):
    self.__authentication_key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)

  enable = __builtin__.property(_get_enable)
  authentication_key = __builtin__.property(_get_authentication_key)


  _pyangbind_elements = {'enable': enable, 'authentication_key': authentication_key, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/authentication/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information associated
with authentication
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__enable','__authentication_key',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__authentication_key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'interface-attributes', u'interface', u'authentication', u'state']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/enable (boolean)

    YANG Description: Enables RSVP authentication on the node.
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/enable (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enables RSVP authentication on the node.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_authentication_key(self):
    """
    Getter method for authentication_key, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/authentication_key (string)

    YANG Description: authenticate RSVP signaling
messages
    """
    return self.__authentication_key
      
  def _set_authentication_key(self, v, load=False):
    """
    Setter method for authentication_key, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/authentication/state/authentication_key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_key() directly.

    YANG Description: authenticate RSVP signaling
messages
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)""",
        })

    self.__authentication_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_key(self):
    self.__authentication_key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)

  enable = __builtin__.property(_get_enable)
  authentication_key = __builtin__.property(_get_authentication_key)


  _pyangbind_elements = {'enable': enable, 'authentication_key': authentication_key, }


