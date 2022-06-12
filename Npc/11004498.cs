using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004498: Lyton
/// </summary>
public class _11004498 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012384$
    // - Who's there? Oh, you're that... that $MyPCName$ hero!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012385$
                // - Who's there? Oh, you're that... that $MyPCName$ hero!
                switch (selection) {
                    // $script:1227192907012386$
                    // - What are you doing here?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012387$
                // - I'm the foremost cultural anthropologist of Sky Fortress, here to study the cultures of Kritias. And I feel I've already made a great discovery!
                return 11;
            case (11, 1):
                // $script:1227192907012388$
                // - I've uncovered some ancient writings here, and the motifs and archetypes on display are similar to those in ancient Victoria Island literature. Uncannily so.
                switch (selection) {
                    // $script:1227192907012389$
                    // - That seems a little unlikely.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012390$
                // - It begs the question: do our cultures share the same root? Of course, the higher-ups will only accept evidence that our culture came first, and that Kritias copied us...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
