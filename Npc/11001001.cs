using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001001: Fredrik
/// </summary>
public class _11001001 : NpcScript {
    internal _11001001(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0424144807008437$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0424144807008438$ 
                // - Hello, $MyPCName$!
                return true;
            default:
                return true;
        }
    }
}
