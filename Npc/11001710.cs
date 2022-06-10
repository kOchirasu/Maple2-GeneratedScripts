using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001710: Tinchai
/// </summary>
public class _11001710 : NpcScript {
    internal _11001710(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006962$ 
                // - Mm?
                return true;
            case 30:
                // $script:0728024507006992$ 
                // - Were your contacts any good this time?
                switch (selection) {
                    // $script:0805021607007084$
                    // - Your informants are little cuties.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0805021607007085$
                    // - Is their information reliable?
                    case 1:
                        Id = 40;
                        return false;
                }
                return true;
            case 31:
                // $script:0805021607007086$ 
                // - I suppose they are! Don't judge them by their looks, though. They've got a knack for gathering information.
                switch (selection) {
                    // $script:0805021607007087$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 40:
                // $script:0805021607007088$ 
                // - I can't think of any reason it wouldn't be. If you're worried, I'll vouch for them personally. They've never failed me in the past.
                switch (selection) {
                    // $script:0805021607007089$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
