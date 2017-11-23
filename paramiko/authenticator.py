"""
Authentication logic module.

Largely replaces what used to be implemented solely within `SSHClient` and its
``_auth()`` method.

Technically, this module's main API member - `Authenticator` - sits below
`SSHClient` (meaning it could theoretically be used by non-Client-based code)
and above `Transport` (which provides the bare auth SSH message 'levers' only.)
"""

class Authenticator(object):
    """
    Wraps a `Transport` and uses it to authenticate, or die trying.

    Lifecycle is relatively straightforward:

    - Instantiate with a handle onto a `Transport` object. This object must
      already have been prepared for authentication by calling
      `Transport.start_client`.
    - Call the instance's `authenticate_with_kwargs` method with as many or few
      auth-source keyword arguments as needed, which will:
        - attempt to authenticate in a documented order of preference
        - if successful, return an `AuthenticationResult`
        - if unsuccessful or if additional auth factors are required, raise an
          `AuthenticationException` (or subclass thereof) which will exhibit a
          ``.result`` attribute whose value is an `AuthenticationResult`.
        - either way, the point is that the caller will have access to an
          `AuthenticationResult` object exposing the various auth sources
          tried, what order they were tried in, and what the result was.
        - see API docs for `authenticate` for further details.
    - Alternately, for tighter control of which auth sources are tried and in
      what order, call `authenticate` directly (it's what implements the guts
      of `authenticate_with_kwargs`) which foregoes most kwargs in lieu of an
      iterable containing `AuthSource` objects.
    """
    def __init__(self, transport):
        # TODO: probably sanity check transport state and bail early if it's
        # not ready.
        # TODO: consider adding some more of SSHClient.connect (optionally, if
        # the caller didn't already do these things) like the call to
        # .start_client
        pass

    def authenticate_with_kwargs(self, lots-o-kwargs-here):
        # Basically SSHClient._auth signature...then calls
        # sources_from_kwargs() and stuffs result into authenticate()?
        # TODO: at the start, just copypasta/tweak SSHClient._auth so the
        # break-up is tested; THEN move to the newer cleaner shit?
        # TODO: this is probably a good spot to reject the
        # password-as-passphrase bit; accept distinct kwargs and require
        # SSHClient to implement the fallback on its end.
        pass

    def authenticate(self, iterable):
        # TODO: define AuthSource (maybe rename...lol), should be lightweight,
        # pairing an auth type with some value or iterable of values
        # TODO: implement cleaner version of SSHClient._auth, somehow, that
        # handles multi-factor auth much better than the current shite
        # trickledown. (Be very TDD here...! Perhaps wait until single-source
        # tests all pass first, then can ensure they continue to do so?)
        pass

    def sources_from_kwargs(self, kwargs):
        # TODO: **kwargs? whatever, this is mostly internal
        # TODO: this should implement, and document, the current (and/or then
        # desired) way that a pile of kwargs becomes an ordered set of
        # attempted auths...
        pass
