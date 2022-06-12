using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000457: Yuri
/// </summary>
public class _11000457 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002034$
    // - What? Is there something you want to ask me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002037$
                // - It's such a nice day to go for a walk or get some juice, but my dumb lump of a boyfriend wants to stay inside. Look at him, he's not even doing anything! Can you convince him to do something with his life?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
