using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000225: Old Man Maneux
/// </summary>
public class _11000225 : NpcScript {
    internal _11000225(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000979$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407000982$ 
                // - Love isn't just about being with someone. Sometimes it's about their memory, too... 
                return true;
            default:
                return true;
        }
    }
}
