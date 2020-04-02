import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='EPUIKit',
    version='0.0.1',
    description='UIKit for Raspberry on E-Paper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='raspberry epaper uikit',
    install_requires=[
        'PIL', 'interval'
    ],
    packages=setuptools.find_packages(),
    author='jinsihou',
    author_email='540097546@qq.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Raspberry :: EPaper',  # 给模块加话题标签
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
