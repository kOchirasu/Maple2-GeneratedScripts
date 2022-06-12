using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001493: Startz
/// </summary>
public class _11001493 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0118150907005809$
    // - I think I'd like to talk today.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005812$
                // - Everything happens for a reason.
                switch (selection) {
                    // $script:0120154307005850$
                    // - Tell me about your past.
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0120154307005851$
                // - Ah, you want to know what happened back then.
                return -1;
            case (32, 0):
                // $script:0120154307005852$
                // - I can't remember.
                return -1;
            case (40, 0):
                // $script:0127102807005856$
                // - Everything happens for a reason.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
