using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004299: Ghost
/// </summary>
public class _11004299 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011387$
    // - Everything in its place. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011390$
                // - A guest came the other day, but I haven't seen him lately. I do hope he's having a nice visit.
                switch (selection) {
                    // $script:1002141907011391$
                    // - Who are you talking about?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011392$
                // - A gentleman with a large briefcase. None of the other ghosts recognized him, but it seems that he was an acquaintance of mademoiselle.
                switch (selection) {
                    // $script:1002141907011393$
                    // - Mademoiselle?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1002141907011394$
                // - Yes, the lady of the hotel. There were evil thoughts in her mind when she met the gentleman. A ghost has a sixth sense about these things, you know.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
