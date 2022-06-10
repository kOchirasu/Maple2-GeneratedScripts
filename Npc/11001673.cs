using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001673: Tinchai
/// </summary>
public class _11001673 : NpcScript {
    internal _11001673(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0711210007006723$ 
                // - Hah... I can barely breathe...
                return true;
            case 30:
                // $script:0727223007006898$ 
                // - Now isn't a great time to talk!
                switch (selection) {
                    // $script:0727223007006899$
                    // - What are these things?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006900$ 
                // - Whatever they are, they aren't good. Let's focus less on what they are and more on how to stop them.
                return true;
            default:
                return true;
        }
    }
}
