using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001499: Dunba
/// </summary>
public class _11001499 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0118150907005832$
    // - Hello!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005835$
                // - Do you happen to know where I can find $map:02010053$? It's got to be around here somewhere.
                switch (selection) {
                    // $script:0120134507005846$
                    // - Why do you ask?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0120134507005847$
                // - I heard they're holding a big grand opening event. Anyone who brings in this handout gets all they can eat for just 5,000 mesos.
                switch (selection) {
                    // $script:0120134507005848$
                    // - It's right up this escalator!
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0120134507005849$
                // - Aw man, the escaltor is out. I didn't sign up for <i>stairs</i>...
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
