using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004522: Friendly Soldieretto
/// </summary>
public class _11004522 : NpcScript {
    internal _11004522(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012492$ 
                // - Beeep... Beeep...
                return true;
            case 40:
                // $script:0104140207012576$ 
                // - Beeep... Beeep...
                return true;
            case 10:
                // $script:0103163407012493$ 
                // - Initiating greeting protocol! The weather is nice today, is it not?
                switch (selection) {
                    // $script:0103163407012494$
                    // - How's your work coming?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0103163407012495$ 
                // - Initiating reassurance protocol! We soldierettos are doing our best. You can count upon us.
                // $script:0103163407012496$ 
                // - Initiating gratitude protocol! We are grateful to the humans who gave us new purpose.
                // $script:0103163407012497$ 
                // - Initiating brusque farewell protocol! This time has been very pleasant, but I have over one hundred tasks remaining for today. Please excuse me.
                switch (selection) {
                    // $script:0103163407012498$
                    // - I'll leave you to it, then.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0103163407012499$ 
                // - Scanning records on aetherine air brake experiment... Scan complete.
                return true;
            case 50:
                // $script:0104140207012577$ 
                // - Initiating excitement protocols! Oh, I have uncovered records about Vanheim. Archiving now.
                return true;
            default:
                return true;
        }
    }
}
