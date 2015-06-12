# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# See http://wiki.archlinux.org/index.php/Python_Package_Guidelines for more
# information on Python packaging.

# Maintainer: Your Name <youremail@domain.com>
pkgname=markbook
pkgver=0.0.1
pkgrel=1
pkgdesc="TODO"
arch=('any')
url=""
license=('custom')
depends=(
  'python' 'python-flask' 'python-flask-script' 'python-flask-sqlalchemy'
  'python-markdown'
)
makedepends=('python-setuptools')
provides=("$pkgname")
source=("${pkgname}-${pkgver}.tar.gz")

package() {
  cd "${pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
