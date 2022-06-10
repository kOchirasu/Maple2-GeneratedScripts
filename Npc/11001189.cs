using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001189: Wei Hong
/// </summary>
public class _11001189 : NpcScript {
    internal _11001189(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1015162707004153$ 
                // - Betrayal is the quickest path to death.
                return true;
            case 30:
                // $script:1015162707004156$ 
                // - So what, they stole one of our trains? Quit whining.
                //   I haven't survived the criminal underworld this long by panicking every time someone came after me!
                return true;
            default:
                return true;
        }
    }
}
