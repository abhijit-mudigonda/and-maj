#Hi Yilun!

wget https://packages.gurobi.com/9.0/gurobi9.0.0_linux64.tar.gz

md5hash=$(md5sum gurobi9.0.0_linux64.tar.gz | awk '{print $1;}')
if [ "$md5hash" != "7878cc518522762d57ed160b3b29287a" ];
then
    echo "md5hash isn't right"
    exit N
fi

echo "md5hash is fine"

tar -xvzf gurobi9.0.0_linux64.tar.gz --exclude='gurobi900/linux64/docs/*' --exclude='gurobi900/linux64/examples/*' --exclude='gurobi900/linux64/matlab/*'
printf 'export GUROBI_HOME="${HOME}/gurobi900/linux64"\nexport PATH="${PATH}:${GUROBI_HOME}/bin" \nexport LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"' >> .bashrc
source .bashrc

grbgetkey d3a69eaa-3070-11ea-8d94-0a7c4f30bdbe

cd ${HOME}/gurobi900/linux64
sudo python setup.py install
cd ${HOME}

echo "Installation of gurobi should be done."

git clone https://github.com/abhijit-mudigonda/and-maj 
cd and-maj
python sscript.py -solver "gurobi"

