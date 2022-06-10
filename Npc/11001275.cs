using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001275: Branko
/// </summary>
public class _11001275 : NpcScript {
    internal _11001275(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1207123607004824$ 
                // - The air here is cleaner than in $map:2000270$.
                return true;
            case 30:
                // $script:1207123607004827$ 
                // - Yes? What do you want?
                switch (selection) {
                    // $script:1207123607004828$
                    // - I heard you're Maccan's assistant.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1207123607004829$ 
                // - Yes. What of it? If you want to ask <i>why</i> I'm still working as Dr. $npcName:11001276[gender:0]$'s assistant, save your breath.
                switch (selection) {
                    // $script:1207123607004830$
                    // - Why are you sti— Oh.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1207123607004831$ 
                // - I knew it! Some people just can't open their mouths without letting a stupid question slip out.
                return true;
            default:
                return true;
        }
    }
}
