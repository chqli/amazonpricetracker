from distutils.core import setup

setup(name='amazonpricetracker',
      version='1.0',
      description='Based on recent sales and recent average costs, provides an algorithm to suggest new cost',
      author='Nirav Pranami',
      packages=['distutils', 'distutils.command'], requires=['aiohttp', 'pyzmq', 'flask', 'flask-restful']
      )
