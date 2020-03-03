# Install required plugins
required_plugins = ["vagrant-hostsupdater"]
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|
  config.vm.define "python" do |python|
    python.vm.box = "ubuntu/bionic64"
    python.vm.network "private_network", ip: "192.168.10.100"
    python.hostsupdater.aliases = ["development.local"]
    python.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "/vagrant/app/playbook.yml"
    end
    python.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
  end
end
