using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000892: Naina
/// </summary>
public class _11000892 : NpcScript {
    internal _11000892(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003260$ 
                // - Ugh... I'm still half asleep...  
                return true;
            case 20:
                // $script:0831180407003261$ 
                // - May the light of the forest be with you. 
                return true;
            default:
                return true;
        }
    }
}
