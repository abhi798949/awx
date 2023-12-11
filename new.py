from ansible import context
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager

# Set the path to the playbook file
playbook_path = 'your_playbook.yml'

# Create a DataLoader object to load YAML content
loader = DataLoader()

# Create an InventoryManager object to manage inventory
inventory = InventoryManager(loader=loader, sources='localhost,')

# Create a VariableManager object to manage variables
variable_manager = VariableManager(loader=loader, inventory=inventory)

# Set the appropriate context
context.CLIARGS = {}

# Create a PlaybookExecutor object
playbook_executor = PlaybookExecutor(
    playbooks=[playbook_path],
    inventory=inventory,
    variable_manager=variable_manager,
    loader=loader,
)

# Run the playbook
results = playbook_executor.run()

# Print the results
print(results)
