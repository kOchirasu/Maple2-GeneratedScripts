using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004227: Roca
/// </summary>
public class _11004227 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010804$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010805$
                // - Sigh... I can't go in there without my squad, but my friends are all no-shows and I'm starting to get pretty bored.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
