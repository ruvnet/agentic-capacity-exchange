from setuptools import setup, find_packages

setup(
    name='distexgpu',
    version='0.1.0',
    description='A client library for interacting with the decentralized GPU marketplace platform.',
    author='Agile Agents Team',
    author_email='support@agileagents.ai',
    packages=find_packages(),
    install_requires=[
        'httpx>=0.21.1',
        'pydantic>=1.8.2',
        'gradio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='gpu, decentralized, marketplace, client',
    python_requires='>=3.8',
)
