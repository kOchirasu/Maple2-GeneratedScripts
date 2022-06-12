using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001080: Yovo
/// </summary>
public class _11001080 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1216233107005208$
    // - The desert hides many secrets, and I'm going to uncover them all!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1216233107005211$
                // - You can feel it, too, can't you? There's something wrong here. You have sharp senses for a human.
                switch (selection) {
                    // $script:1216233107005212$
                    // - What is this strange energy?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1216233107005213$
                // - I wouldn't get too curious about it if I were you. In fact, keep your distance unless you have some good info for me. I don't have time to answer questions for ignoramuses.
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
