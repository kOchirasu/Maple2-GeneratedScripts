using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000121: Daniel
/// </summary>
public class _11000121 : NpcScript {
    internal _11000121(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000521$ 
                // - What is it?
                return true;
            case 50:
                // $script:0831180407000526$ 
                // - Each of the monsters from the Land of Darkness has unique genetic material. By analyzing a wide range of material, I'm hoping to determine the rules that differentiate them from Maple World's monsters.
                return true;
            default:
                return true;
        }
    }
}
