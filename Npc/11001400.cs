using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001400: Martino
/// </summary>
public class _11001400 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217193307005400$
    // - What brings you here? C'mon, let's hear it!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228164407005736$
                // - A high salary is good, but there are other important factors when choosing a job. Comfort, for instance. And safety... I've made a terrible mistake...
                switch (selection) {
                    // $script:1228164407005737$
                    // - What's wrong?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1228164407005738$
                // - Where do I begin?! How about the fact that I can't get out of this death trap!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
