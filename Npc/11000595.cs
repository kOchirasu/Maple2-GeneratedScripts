using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000595: Scott
/// </summary>
public class _11000595 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002385$
    // - Hm... That's... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002389$
                // - Mm? Are you a traveler?
                switch (selection) {
                    // $script:0831180407002390$
                    // - What are you doing here?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0831180407002391$
                // - Oh, me? I'm studying these creatures we call the fairfolk. All kinds of fairfolk inhabit forests like this.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
