using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000132: Yentayo
/// </summary>
public class _11000132 : NpcScript {
    internal _11000132(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000787$ 
                // - What seems to be the problem?
                return true;
            case 10:
                // $script:1121222006000788$ 
                // - What seems to be the problem?
                return true;
            default:
                return true;
        }
    }
}
