using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003960: Wizard
/// </summary>
public class _11003960 : NpcScript {
    internal _11003960(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010011$ 
                // - They have so many tasty foods here! 
                return true;
            case 20:
                // $script:0614143707010012$ 
                // - Hey... Do you have more Orange Mushroom cookies...? I ate all of mine, hehe. 
                return true;
            default:
                return true;
        }
    }
}
