using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000247: Alfred
/// </summary>
public class _11000247 : NpcScript {
    internal _11000247(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000805$ 
                // - What seems to be the problem? 
                return true;
            case 10:
                // $script:1121222006000806$ 
                // - What seems to be the problem? 
                return true;
            default:
                return true;
        }
    }
}
