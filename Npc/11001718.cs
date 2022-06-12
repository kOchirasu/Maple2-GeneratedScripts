using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001718: Junta
/// </summary>
public class _11001718 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006969$
    // - You have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0805021607007100$
                // - Not all questions require an answer. Some mysteries are better left unsolved. But even I have trouble when to seek the truth, and when to let an issue lie...
                switch (selection) {
                    // $script:0805021607007101$
                    // - What are you talking about?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0805021607007102$
                // - Never mind. I've just had much on my mind lately...
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
