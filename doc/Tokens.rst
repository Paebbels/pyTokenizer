Tokens
######

A ``Token`` is a chain of characters forming a coherent text unit in a document.

Token
*****

This class implements the base-class for all token classes.

.. rubric:: Inheritance diagram:

.. inheritance-diagram:: pyTokenizer.SuperToken pyTokenizer.ValuedToken pyTokenizer.StartOfDocumentToken pyTokenizer.CharacterToken pyTokenizer.SpaceToken pyTokenizer.DelimiterToken pyTokenizer.NumberToken pyTokenizer.StringToken
   :parts: 1

.. autoclass:: pyTokenizer.Token
   :show-inheritance:
   :members:
   :private-members:



SuperToken
**********

.. autoclass:: pyTokenizer.SuperToken
   :show-inheritance:
   :members:
   :private-members:



ValuedToken
***********

.. autoclass:: pyTokenizer.ValuedToken
   :show-inheritance:
   :members:
   :private-members:



StartOfDocumentToken
********************

A topken stream starts with a ``StartOfDocumentToken``.

.. autoclass:: pyTokenizer.StartOfDocumentToken
   :show-inheritance:
   :members:
   :private-members:



CharacterToken
**************

.. autoclass:: pyTokenizer.CharacterToken
   :show-inheritance:
   :members:
   :private-members:



SpaceToken
**********

.. autoclass:: pyTokenizer.SpaceToken
   :show-inheritance:
   :members:
   :private-members:



DelimiterToken
**************

.. autoclass:: pyTokenizer.DelimiterToken
   :show-inheritance:
   :members:
   :private-members:



NumberToken
***********

A ``NumberToken`` represents a number (RegExp: ``[0-9]+``).

.. autoclass:: pyTokenizer.NumberToken
   :show-inheritance:
   :members:
   :private-members:



StringToken
***********

A ``StringToken`` represents a word (RegExp: ``[a-zA-Z]+``).

.. autoclass:: pyTokenizer.StringToken
   :show-inheritance:
   :members:
   :private-members:
