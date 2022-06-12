using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000695: Bazette
/// </summary>
public class _11000695 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002802$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002806$
                // - Making potions is very difficult. The first priority is preparing the ingredients. You need very specific ingredients to make effective potions.
                return 50;
            case (50, 1):
                // $script:0831180407002807$
                // - Some people compare potion brewing to cooking. They're crazy if they think potions are as easy to make as food.
                return 50;
            case (50, 2):
                // $script:0831180407002808$
                // - Here, I'll give you an example. Say you're making fried rice. You can put in just about anything you want. Ham, peppers, carrots, anything you want.
                return 50;
            case (50, 3):
                // $script:0831180407002809$
                // - When you're making a potion, however, you must add the ingredients in the correct order, at the correct time. You can't take your eyes off the cauldron.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.Next,
            (50, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
