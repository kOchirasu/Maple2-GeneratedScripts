using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001369: Livet
/// </summary>
public class _11001369 : NpcScript {
    internal _11001369(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1110153306000979$ 
                // - Hello, hello, hello! I'm <i>triple</i> happy to see you! 
                return true;
            case 30:
                // $script:1110153306000982$ 
                // - Amazing that such a glorious city can thrive here, don't you think?
                return true;
            default:
                return true;
        }
    }
}
