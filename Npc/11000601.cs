using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000601: Luanna
/// </summary>
public class _11000601 : NpcScript {
    internal _11000601(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002468$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407002473$ 
                // - The world is relying on your strength. May the empress's blessing be with you.
                return true;
            case 40:
                // $script:1215105907009721$ 
                // - Empress's blessings, $MyPCName$! What brings you here?
                switch (selection) {
                    // $script:1215105907009722$
                    // - I've heard a lot of rumors circulating through town.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1215105907009723$ 
                // - Ah, yes, as have we. A dark aura begins to spread over Maple World once more.
                switch (selection) {
                    // $script:1215105907009724$
                    // - Tell me what you know.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1215105907009725$ 
                // - I'm afraid I have no more information than anyone else. However... I sense that the strange occurrences of late are harbingers of a greater darkness. A threat unlike any we have faced.
                // $script:1215105907009726$ 
                // - Please... be careful.
                return true;
            default:
                return true;
        }
    }
}
