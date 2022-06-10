using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003872: Bedd
/// </summary>
public class _11003872 : NpcScript {
    internal _11003872(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009860$ 
                // - What's more important? The process? Or the results?
                return true;
            case 10:
                // $script:0417135107009861$ 
                // - I guess you need good process <i>and</i> solid results.
                return true;
            default:
                return true;
        }
    }
}
