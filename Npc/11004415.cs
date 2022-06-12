using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004415: Frosty Fairfolk
/// </summary>
public class _11004415 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1120173007011889$
    // - The fairfolk's cake is so, so sweet!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1120173007011892$
                // - The fairfolk's cake is so, so sweet!
                return 10;
            case (10, 1):
                // $script:1120173007011894$
                // - Eat all you want, and it never never runs out! It's <i>magic cake</i>. That's the best part! Hee hee!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
