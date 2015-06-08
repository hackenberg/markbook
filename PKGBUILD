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
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
provides=('markbook')
source=("$pkgname-$pkgver.tar.gz")

#build() {
#  cd "$pkgname-$pkgver"
#  python setup.py build
#}

package() {
  depends=('python-flask', 'python-markdown')
  cd "$pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1
}

# vim:set ts=2 sw=2 et:
