using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001073: Wild Feet
/// </summary>
public class _11001073 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003659$
    // - Toh! Toh! Toh!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003662$
                // - I don't talk to those who do not practice martial arts.
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
