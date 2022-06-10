using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004137: Mysterious Bladesman
/// </summary>
public class _11004137 : NpcScript {
    internal _11004137(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010539$ 
                // - Forget it.
                return true;
            case 10:
                // $script:0730132107010540$ 
                // - This is nothing.
                return true;
            default:
                return true;
        }
    }
}
