using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000389: Tivo
/// </summary>
public class _11000389 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001581$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001584$
                // - Since the big split, $map:2000115$ has been attracting all kinds of lookie-loos. And a true businessman never wastes a good opportunity like this!
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
