# NOTE: GSSAPI is kind of a standalone feature and is tested elsewhere.

#
# Edge/error cases that aren't strongly tied to a given success case
#

class BadAuth:
    def 


#
# Single auth sources
#

class NullAuth:
    # Yup, it's a thing!

    def ugh_remove_me(self):
        pass


class PasswordAuth:
    pass


class InteractiveAuth:
    # TODO: how exactly is auth_interactive different from auth_password?
    # TODO: and what's the diff between transport's interactive vs
    # interactive_dumb?
    # TODO: and how (is?) it different from what's used for TOTP
    pass


class UnencryptedPublicKeyAuth:
    pass


class EncryptedPublicKeyAuth:
    pass


#
# Multiple auth sources, of which only one is needed/valid
#

class ManyAuthsEnterOneAuthLeaves:
    pass


#
# True multi-factor auth, where more than one source is needed/required
#

class MultiFactorAuth:
    pass
